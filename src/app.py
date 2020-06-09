""" ETL API app entry point """
import logging
import sys
from commands.factory import get_command

from flask import Flask

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def index():
    return {
        'status': 'ok',
        'msg': 'index route'
    }


@app.route('/etl/<command>/<verbose>')
def do_etl(command, *args, **kwargs):
    """ accept GET request and execute command with the options passed """

    try:
        logging.debug('kwargs=%s', kwargs)
        _opts = api_kwargs_to_options(**kwargs)
        logging.info('Executing %s with options %s', command, _opts)

        cmd = get_command(command)

        logging.debug('Found %s', cmd)

        cmd(_opts)
    except Exception as ex:
        return {"status": "err", "msg": repr(ex)}

    return {"status": "ok"}


def api_kwargs_to_options(**kwargs):
    """ convert kwargs to options """

    verbose = True if 'verbose' in kwargs and kwargs['verbose'] != 'False' else False

    return {
        '--verbose': verbose,
        '--conn': 'sqlite:///:memory:',
        '--file': '../data/inbound/KPHX_with_reserved.dat'
    }
