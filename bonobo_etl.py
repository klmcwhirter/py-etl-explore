
from bonobo.config import use, requires
import bonobo


def get_services(**kwargs):
    return {
        'datareader': bonobo.CsvReader(
            kwargs['filename'],
            delimiter='|',
            fields=['id', 'city', 'date', 'actual_mean_temp', 'actual_min_temp', 'actual_max_temp',
                    'actual_precipitation', 'average_precipitation', 'record_precipitation', 'reserved2']
        ),
        'filename': kwargs['filename']
    }


def arg0_to_kwargs(**row):
    return {**row}

@use('filename')
@use('datareader')
def read_recs(filename, datareader):
    print(type(datareader))
    for rec in datareader.read(filename):
        yield rec

def transform(**row):
    print(f'transform ...')
    return {**row}

def write_recs(**row):
    print(f'write_recs: {row}')

graph = bonobo.Graph(
    bonobo.CsvReader(
        'KPHX.dat',
        delimiter='|',
        fields=['id', 'city', 'date', 'actual_mean_temp', 'actual_min_temp', 'actual_max_temp',
                'actual_precipitation', 'average_precipitation', 'record_precipitation', 'reserved2']
    ),
    arg0_to_kwargs,
    transform,
    write_recs)

bonobo.run(graph, services=get_services(filename='KPHX.dat'))

graph.add_chain(
    bonobo.PrettyPrinter(),
    _input=arg0_to_kwargs
)