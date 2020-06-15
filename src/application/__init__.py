""" ETL API app entry point """
import logging
import sys
from commands.factory import get_command

from flask import Flask

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)

app = Flask(__name__)

from application import views
