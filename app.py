""" ETL API app entry point """

from commands import get_command

from flask import Flask

app = Flask(__name__)


@app.route('/etl/<command>/<path:options>')
def do_etl(command, options):
    """ accept GET request and execute command with the options passed """

    cmd = get_command(command)
    cmd(options)
