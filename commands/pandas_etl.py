"""a simple ETL modulle

Usage:
    pandas_etl.py load [--conn=<conn-string>] [--file=<file>] [-v | --verbose]

Options:
  --conn=<conn-string>  The connection string to use. e.g., sqlite:///pandas_etl.db [default: sqlite:///:memory:]
  --file=<file>         The file to process [default: data/inbound/KPHX_with_reserved.dat]
  -v, --verbose         More verbose output [defaut: false]
  -h --help             Show this screen.
  --version             Show version.

"""

import logging
import sys

import pandas as pd
from docopt import docopt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.weather import Base, Weather


class PandasEtlCommand(object):
    """ Command for Pandas ETL """

    def __init__(self):
        """ initialize command """

    def __call__(self, *args, **kwargs):
        """The main program"""

        print(f'PandasEtlCommand: {args}')

        verbose = args[0]['--verbose'] if args[0]['--verbose'] else False

        llevel = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            stream=sys.stdout, format='%(asctime)s %(levelname)s %(message)s', level=llevel)

        if verbose:
            logging.debug(args)

        conn_string = args[0]['--conn']
        logging.debug(f'setting conn_string to "{conn_string}"')

        # Populate from file
        df_with_reserved = pd.read_table(
            args[0]['--file'], sep='|', header=0,
            usecols=[
                'id', 'city', 'date', 'actual_mean_temp', 'actual_min_temp', 'actual_max_temp',
                'actual_precipitation', 'average_precipitation', 'record_precipitation', 'reserved2'
            ],
            dtype={
                'id': 'int', 'city': 'string',
                # 'date': '?', # let parser handle the converion - see https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv
                'actual_mean_temp': 'int8', 'actual_min_temp': 'int8', 'actual_max_temp': 'int8',
                # 'actual_precipitation','average_precipitation','record_precipitation',
                'reserved2': 'string'
            },
            # These next three are needed to parse and optimize datetime input handling
            parse_dates=[2],
            infer_datetime_format=True,
            date_parser=pd.to_datetime
        )

        # Create the engine --> echo=True utiizes the integration with Python logging to display SQL
        # To make the output more brief set ```echo=False```.

        engine = create_engine(conn_string, echo=verbose)

        # We do not want to do this in production - it creates the tables ...
        Base.metadata.create_all(engine)

        # Make a session
        session = sessionmaker(bind=engine)()

        for _, row in df_with_reserved.iterrows():
            weather = Weather(**row)
            if verbose:
                logging.debug(weather)
            session.add(weather)

        session.commit()


if __name__ == '__main__':
    inst = PandasEtlCommand()
    arguments = docopt(__doc__, version="1.0")
    inst(arguments)
