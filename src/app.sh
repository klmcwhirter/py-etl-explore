#!/bin/bash

cd /opt/src/app/src

source ../venv/bin/activate

flask run --port=8080
