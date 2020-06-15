from io import open
from os.path import exists

import setuptools

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    install_reqs = [line.rstrip("\n") for line in lines]

# TODO: enhance this by calling pip freeze instead to pick up version information for development
if exists('requirements.dev.txt'):
    with open('requirements.dev.txt', 'r') as f:
        lines = f.readlines()
        extras_req_dev = [line.rstrip("\n") for line in lines]
else:
    extras_req_dev = ''

with open('README.md', 'r') as f:
    long_desc = f.read()

setuptools.setup(
    name="py-etl-explore",
    description="exploration project of ETL with Python",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version="0.0.2",

    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},

    install_requires=install_reqs,
    extras_require={
        "dev": extras_req_dev
    },

    classifiers=[
        # https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',

        # Uses f-string - so at least 3.6
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'

        # See LICENSE
        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent'
    ]
)
