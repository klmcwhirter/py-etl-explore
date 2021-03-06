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

import bonobo
from bonobo.config import use
from docopt import docopt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.weather import Weather

# TODO move this line somewhere central ...
csv.register_dialect('pipe_delim', delimiter='|')


class BonoboEtlCommand(object):
    """ Command for Bonobo ETL """

    def __init__(self):
        """ initialize command """

        self.graph = bonobo.Graph(
            self.read_recs,
            self.write_recs
        )

    def __call__(self, *args, **kwargs):
        """ execute command """

        # This is not that useful, but does show how to create more complicated graphs
        # graph.add_chain(
        #     bonobo.PrettyPrinter(),
        #     _input=read_recs
        # )

        services = self.get_services(args[0])

        engine = services['sqlalchemy.engine']

        # We do not want to do this in production - it creates the tables ...
        Weather.metadata.create_all(engine)

        # Make a session
        session = sessionmaker(bind=engine)()

        # Add it to injectable services
        services['session'] = session

        bonobo.run(self.graph, services=services)

        session.commit()

    def get_services(self, *args):
        """ provide services that can be injected """

        verbose = args[0]['--verbose'] if args[0]['--verbose'] else False

        llevel = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            stream=sys.stdout, format='%(asctime)s %(levelname)s %(message)s', level=llevel)

        logging.debug(args)

        return {
            **args[0],
            'verbose': verbose,
            'filename': args[0]['--file'],
            'fieldnames': ['id', 'city', 'date',
                           'actual_mean_temp', 'actual_min_temp', 'actual_max_temp',
                           'actual_precipitation', 'average_precipitation',
                           'record_precipitation', 'reserved2'],
            'sqlalchemy.engine': create_engine(args[0]['--conn'], echo=verbose),
        }

    @use('filename', 'fieldnames')
    # @use('fieldnames')
    def read_recs(self, filename, fieldnames):
        """ read recs using streaming protocol """
        with open(filename, newline='') as _f:
            reader = csv.DictReader(
                _f, dialect='pipe_delim', fieldnames=fieldnames)
            next(reader, None)  # skip header row
            for row in reader:
                logging.info('read_recs: row=%s', row)

                del row[None]  # remove unused fields

                weatherrec = Weather(**row)  # use kwargs expansion of the dict

                weatherrec.date = datetime.strptime(row['date'], '%Y-%m-%d')

                logging.info('read_recs: weatherrec=%s', weatherrec)

                yield weatherrec

    @use('session')
    def write_recs(self, rec, session):
        """ write recs as provided """
        logging.info('write_recs: rec=%s', rec)

        session.add(rec)


if __name__ == '__main__':
    inst = BonoboEtlCommand()
    arguments = docopt(__doc__, version='1.0')
    inst(arguments)
