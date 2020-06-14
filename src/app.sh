#!/bin/bash

pushd src

source ../venv/bin/activate

flask run --port=8080

popd
