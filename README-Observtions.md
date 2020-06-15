# Python ETL Explore

A place to explore using Python for ETl.

## K8S Jobs :-1:
The [Job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) concept in Kubernetes (K8S) is ill conceived.

It assumes that a job runs to completion and that is it. A Job cannot be re-run.

This means that to run a job again it needs to be deleted and defined / run again.

So if a Job needs to be scheduled from another (external) scheduler it must be deleted and redefined.

This fact means the K8S Job concept does not allow for the concept to integrate well with popular enterprise solutions.

Execute etc/run_jobs.sh to see what I mean. Try to apply the yaml without deleting for example.

And it seems that the output is not successfully captured in most cases; meaning the log will be incomplete.


## API in OpenShift
...

## Docker / podman
...
