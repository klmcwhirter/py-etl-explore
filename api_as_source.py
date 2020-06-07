import pprint
from time import sleep

import bonobo
import requests
from bonobo.config import use


def get_services():
    return {
        'randomusers_baseurl': 'https://randomuser.me/api/',
        'num_results': 5,
        'pprinter': pprint.PrettyPrinter()
    }

@use('randomusers_baseurl')
@use('num_results')
def get_n_users(randomusers_baseurl, num_results):
    url = f'{randomusers_baseurl}?results={num_results}'
    print(f'url={url}')
    response = requests.get(url)
    if response.ok:
        data = response.json()
        if data['info']['results']:
            for rec in data['results']:
                yield rec

@use('pprinter')
def pprint_rec(rec, pprinter):
    s = pprinter.pformat(rec)
    print(f'{s}\n#*------------------------------------------------------------*')

graph = bonobo.Graph(
    get_n_users,
    pprint_rec
)

bonobo.run(graph, services=get_services())

sleep(5) # give output time to get into the logs
