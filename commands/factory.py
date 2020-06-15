""" Commands available """

from .api_as_source import ApiAsSourceCommand
from .bonobo_etl import BonoboEtlCommand
from .pandas_etl import PandasEtlCommand

COMMANDS = {
    "api_as_source": ApiAsSourceCommand,
    "bonobo_etl": BonoboEtlCommand,
    "pandas_etl": PandasEtlCommand
}

__all__ = ['get_command']


def get_command(name):
    """ return command represented by name """

    _rc = COMMANDS[name]()
    return _rc
