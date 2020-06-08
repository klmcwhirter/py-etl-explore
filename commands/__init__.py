""" Commands available """

from .api_as_source import ApiAsSourceCommand

COMMANDS = {
    "api_as_source": ApiAsSourceCommand
}

__all__ = ['get_command']


def get_command(name):
    """ return command represented by name """

    _rc = COMMANDS[name]()
    return _rc
