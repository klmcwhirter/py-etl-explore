""" ETL API app entry point """
import logging
import sys
from commands.factory import get_command

from flask import Flask

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)

app = Flask(__name__)


@app.route('/etl/<command>/<path:options>')
def do_etl(command, **options):
    """ accept GET request and execute command with the options passed """

    try:
        logging.debug('options=%s', options)
        _opts = dict(options)
        logging.info('Executing %s with options %s', command, _opts)

        cmd = get_command(command)

        logging.debug('Found %s', cmd)
        print(cmd.__module__.__doc__)

        cmd(_opts)
    except Exception as ex:
        return {"status": "err", "msg": repr(ex)}

    return {"status": "ok"}
