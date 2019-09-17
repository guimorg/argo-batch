# Batch Serving - Machine Learning

## Introduction

This is a simple project designed to implement the use of Argo to train and make predictions using a Machine Learning model. Here we have a basic DAG consisting of three steps:

1. Getting train data from a bucket
2. Training the model
3. Make predictions using a test dataset

## The model

This model was implemented by [Roshan Sharma](https://www.kaggle.com/roshansharma) in [Kaggle](https://www.kaggle.com/roshansharma/mall-customers-clustering-analysis) and uses KMeans to target different customers from a Mall based on their incomes and spending score habits. This correlates to the Market Basket Analysis, in which you can predict if a customer will more (or less) likely buy a group of items based on which products he bought (Affinity Analysis).

## The framework

Here we are using Python to make simple scripts that download files from our Artifact Repository (S3 Bucket), to train our model and to make predictions in a dataset. The **huge** thing here is that we are using Argo to manage and orchestrate the Workflow of steps.

Using Argo is very interesting because it already runs in Kubernetes, so, because of that, you win the benefit of running your application in Kubernetes with the benefit of creating dependencies between jobs and worrying only with the logic of the steps

## What you will find here

Here you will find 4 directories:

1. Argo: you will find a simple workflow to run in Argo. To run this you need to have Argo integration with S3 Bucket and also have the .csv file in a S3 bucket. The first step is very important because in each job of this workflow Argo will generate artifacts in your bucket (simulating an Artifact Repository);

2. Data: you have a simple script to download files from a S3 bucket and a Dockerfile, that should generate the image usade by the first step of our workflow!

3. Train: simple script to train the model and to serialize it. Argo makes sure that this artifact is saved in our artifact repository. There is also a Dockerfile to generate the image.

4. Predict: using the trained model, this last step takes a dataset and uses ```.predict``` on it to generate a file with the CustomerID and the group prediction! With a Dockerfile inbound! 

# Author
Guilherme Gimenez Jr
