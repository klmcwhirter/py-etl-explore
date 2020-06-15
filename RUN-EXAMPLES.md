# Python ETL Explore

A place to explore using Python for ETl.


## Running Examples Overview

There are 3 types of executables in this repo.

1. Jupyter notebooks - .ipynb files in Jupyter dir
1. Standalone modules - .py files in the commands dir
1. Flask app hosting API - app.py

## Jupyter Notebooks

Make sure you have created and activated the virtual environment as documented in [0. README](0. README.md).

Select the virtual environment via the command pallete.
```CTRL-SHIFT-P``` - ```Python: Select Interpreter to start Jupyter server```

Open a notebook.

## Standalone Modules

Make sure you have created and activated the virtual environment as documented in [0. README](0. README.md).

```bash
$ python3 -m <module_to_execute> [options]
```

For example:
```bash
$ python3 -m commands.bonobo_etl load --verbose --conn=sqlite:///data/outbound/bonobo_weather.db
$ sqlite3 data/outbound/bonobo_weather.db 'select count(1) from weather' # should output 365
$ rm data/outbound/bonobo_weather.db
```


## Flask App

Make sure you have created and activated the virtual environment as documented in [0. README](0. README.md).

Simply execute:

```bash
$ cd src
$ flask run --port=8080
$ curl http://127.0.0.1:8080/etl/pandas_etl/verbose
```

Console output should show verbose log.

## K8S Jobs
This is a future looking feature that is not panning out so well. I will revisit it later.

If interested the job definitions are in the etc/ dir. But they require deployment into OCP to execute.


Note this repo is setup as an S2I compliant source package. But more to come ...
