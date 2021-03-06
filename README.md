# Python ETL Explore

A place to explore using Python for ETl.

## Overview

When hosted in Linux Docker containers, Python is a valid and reliable choice for ETL work loads.

## Why?

>
> _Enable more junior engineers to perform simple tasks, simpler._
>

Python is a popular choice for data processing. Much progress has been made to raise Python to a place
where it it has become the languge of choice for data scientists world wide.

This is because of language, as well as standard and 3rd party library enhancements enabling it to handle
large data sets as well as complex data procssing jobs.

## TODO
* [x] Determine baseline list of tools
* [x] Create individual scripts for 3 types of ETL
* [x] Refactor as package
* [x] Create K8S Job definitions
* [ ] Create API wrapper that can be used instead of K8S jobs
  * [ ] Introduce AppContext with config (jsonconfig)
* [ ] Introduce conditional logging (console for K8S, file for legacy console) - local framework in app context
* [ ] Introduce setup.py (setuptools) for API K8S service
* [ ] explore testing standards (pytest / rope)
* [ ] port markdown to .rst

## Setup for development

_Note the instructions below are for Linux. Do what is needed for the OS on which you are working._

1. The Python VS Code extension should be installed
1. Create virtual environment - ```python3 -m venv venv```
1. Activate environment - ```source venv/bin/activate```
1. Upgrade pip - ```python3 -m pip install --upgrade pip wheel```
1. Create wheel - ```python3 setup.py bdist_wheel```
1. Install wheel for dev - ```pip install -e .```
1. Install dev extras - ```pip install .[dev]```

## Setup for a prod-like env - just the scripts

_Note the instructions below are for Linux. Do what is needed for the OS on which you are working._

1. Create virtual environment - ```python3 -m venv venv```
1. Activate environment - ```source venv/bin/activate```
1. Upgrade pip - ```python3 -m pip install --upgrade pip wheel```
1. Create wheel - ```python3 setup.py bdist_wheel```
1. Install wheel for dev only - ```pip install -e .```

## Proposed Packages for Consideration

|Package|LINK|Comments|
|--|--|--|
|**_Development tools_**|
|VS Code|[LINK](https://code.visualstudio.com/)|programmer's editor|
|Python Extension|[LINK](https://marketplace.visualstudio.com/items?itemName=ms-python.python)|provided by Microsoft|
|Jupyter notebooks|[LINK](https://code.visualstudio.com/docs/python/jupyter-support)|supported by Python extension; prototyping|
|autorep8|[LINK](https://code.visualstudio.com/docs/python/editing#_formatting)|VS Code integration for code formatting|
|pytest|[LINK](https://code.visualstudio.com/docs/python/testing)|VS Code integration for unit test execution|
|rope|[LINK](https://github.com/python-rope/rope)|VS Code integation - Python refactoring and other VS Code helpers|
|venv|[LINK](https://code.visualstudio.com/docs/python/environments)|Virtual environments (built-in)|
|**_App shell_**|
|docopt|[LINK](http://docopt.org/); [CODE](https://github.com/docopt/docopt)|documentation-first CLI deisgn / parsing; note [.NET port](https://github.com/docopt/docopt.net)|
|logging|[LINK](https://docs.python.org/3/library/logging.html)|built-in; features like NLog|
|flask|[LINK](https://palletsprojects.com/p/flask/); [CODE](https://github.com/pallets/flask/)|for hosting API (_future_)|
|**_Orchestration_**|
|bonobo :+1:|[LINK](https://www.bonobo-project.org/)|Lightweight; flexible; suited for simple tasks|
|airflow :-1:|[LINK](https://airflow.apache.org/); [Intro](https://youtu.be/6eNiCLanXJY); [K8S](https://youtu.be/VrsVbuo4ENE); [K8S](https://youtu.be/A0gKV1r7w8M)|Apache project; developed at Airbnb; k8s integration by Bloomberg; hard to get code reuse; integrations; overlaps with CG enterprise features|
|luigi :-1:|[LINK](https://luigi.readthedocs.io/en/stable/); [CODE](https://github.com/spotify/luigi)|Spotify; lightweight; but classes define job hierarchy|
|argo :-1:|[LINK](https://argoproj.github.io/); [CODE](https://github.com/argoproj/); [K8S](https://youtu.be/99o9S20D5s8); [DEMO](https://youtu.be/JjSp00RsWF0)|built by Intuit|
|**_Database_**|
|sqlalchemy|[LINK](https://www.sqlalchemy.org/)|defacto standard ORM|
|**_Documentation_**|
|mkdocs :+1:|[LINK](https://www.mkdocs.org/)|Markdown docs; more widespread; simpler|
|Sphinx :-1:|[LINK](https://www.sphinx-doc.org/)|ReStuctured Text docs; pythonic; more capable, but more complicated|
|**_Miscellaneous_**|
|pandas|[LINK](https://pandas.pydata.org/)|large data set operations;not very efficient; but complete|
|numpy|[LINK](https://numpy.org/)|industry standard library for numerical types and operations|

## Kudos

We can all thank the work behind:
* numpy
* pandas
* scipy
* scikit-learn
* matplotlib
* tensorflow
* PyTorch
* keras
* Jython
* etc.
