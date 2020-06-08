"""a simple ETL modulle

Usage:
    bonobo_etl.py load [--conn=<conn-string>] [--file=<file>] [-v | --verbose]

Options:
  --conn=<conn-string>  The connection string to use. e.g., sqlite:///data/outbound/pandas_etl.db [default: sqlite:///:memory:]
  --file=<file>         The input file to process [default: data/inbound/KPHX_with_reserved.dat]
  -v, --verbose         More verbose output [defaut: false]
  -h --help             Show this screen.
  --version             Show version.

"""

import csv
import logging
import sys
from datetime import datetime
from time import sleep

import bonobo
from bonobo.config import use
from docopt import docopt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.weather import Weather

# TODO move this line somewhere central ...
csv.register_dialect('pipe_delim', delimiter='|')


def get_services(**kwargs):
    """ provide services that can be injected """

    verbose = kwargs['--verbose'] if kwargs['--verbose'] else False

    llevel = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)s %(message)s', level=llevel)

    logging.debug(kwargs)

    return {
        **kwargs,
        'verbose': verbose,
        'filename': kwargs['--file'],
        'fieldnames': ['id', 'city', 'date',
                       'actual_mean_temp', 'actual_min_temp', 'actual_max_temp',
                       'actual_precipitation', 'average_precipitation',
                       'record_precipitation', 'reserved2'],
        'sqlalchemy.engine': create_engine(kwargs['--conn'], echo=verbose),
    }


@use('filename')
@use('fieldnames')
def read_recs(filename, fieldnames):
    """ read recs using streaming protocol """
    with open(filename, newline='') as f:
        reader = csv.DictReader(f, dialect='pipe_delim', fieldnames=fieldnames)
        next(reader, None)  # skip header row
        for row in reader:
            logging.info(f'read_recs: row={row}')

            del row[None]  # remove unused fields

            weatherrec = Weather(**row)  # use kwargs expansion of the dict

            weatherrec.date = datetime.strptime(row['date'], '%Y-%m-%d')

            logging.info(f'read_recs: weatherrec={weatherrec}')

            yield weatherrec


@use('session')
def write_recs(rec, session):
    """ write recs as provided """
    logging.info(f'write_recs: rec={rec}')

    session.add(rec)


def main(args):
    """ main program """

    graph = bonobo.Graph(
        read_recs,
        write_recs
    )

    # This is not that useful, but does show how to create more complicated graphs
    # graph.add_chain(
    #     bonobo.PrettyPrinter(),
    #     _input=read_recs
    # )

    services = get_services(**args)

    engine = services['sqlalchemy.engine']

    # We do not want to do this in production - it creates the tables ...
    Weather.metadata.create_all(engine)

    # Make a session
    session = sessionmaker(bind=engine)()

    # Add it to injectable services
    services['session'] = session

    bonobo.run(graph, services=services)

    session.commit()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    main(arguments)
