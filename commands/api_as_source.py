""" ApiAsSourceCommand """

import logging
import pprint
import sys

import bonobo
import requests
from bonobo.config import use

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


class ApiAsSourceCommand(object):
    """ Command for api_as_source """

    def __init__(self):
        """ initiaiize command """

        self.graph = bonobo.Graph(
            self.get_n_users,
            self.pprint_rec
        )

    def __call__(self, *args, **kwargs):
        """ perform the command """

        logging.info('Running %s', __name__)

        bonobo.run(self.graph, services=self.get_services())

    def get_services(self):
        """ register injectable services """

        return {
            'randomusers_baseurl': 'https://randomuser.me/api/',
            'num_results': 5,
            'pprinter': pprint.PrettyPrinter()
        }

    @use('randomusers_baseurl')
    @use('num_results')
    def get_n_users(self, randomusers_baseurl, num_results):
        """ get N number random users """

        url = f'{randomusers_baseurl}?results={num_results}'
        logging.info('url=%s', url)
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if data['info']['results']:
                for rec in data['results']:
                    yield rec

    @use('pprinter')
    def pprint_rec(self, rec, pprinter):
        """ pretty print the record """

        _s = pprinter.pformat(rec)
        logging.info('%s\n%s',
                     _s,
                     '#*------------------------------------------------------------*'
                     )


if __name__ == '__main__':
    inst = ApiAsSourceCommand()
    inst()
