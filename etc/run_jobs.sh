#!/bin/bash

oc delete -f ./jobs.yaml

sleep 5 # give some time for the delete to take effect

for j in api_as_source bonobo_etl pandas_etl
do
    oc apply -f ./job-${j}.yaml
    sleep 5
done

# oc logs api-as-source-*
# oc logs bonobo-etl-*
# oc logs pandas-etl-*
