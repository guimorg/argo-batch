# Argo Workflow

Here you will find a basic ```workflow.yaml``` file that sets our DAG. We only have three steps:

1. Downloading files from bucket: input dataset

2. Training our model: artifact generated is a pickle of the model (joblib)

3. Scoring with our model: artifact generated is the file with predictions

## Persistance during Workflow

A nice thing about this workflow is that I implemented a 'temporary persistance' during the execution of the workflow, that way each step can use the PVC to use data from previous steps or save data to be processed by future steps but in the end the claim is deleted and the PVC is done.

## To run this file

To run this workflow make sure you have an artifact repository integrated with Argo or you will have problems with the ```artifacts```
