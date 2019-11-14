# SageMaker Demo
Deploy a model as a REST API using AWS SageMaker, Lambda, and API Gateway.

## Overview
This demo shows you how to build a text-classifier using Amazon SageMaker, and how to deploy it as a REST API. With a few modifications, you can create and API for almost any machine learning problem using this framework.

## Dependencies
* Create an [AWS account](https://aws.amazon.com) if you don't already have one
* [Create an admin user in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
* ``pip install awscli --upgrade --user``
* [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)
* ``pip install boto3``
* ``pip install sagemaker``
* Create an S3 bucket to host your training data and model

## The Data
The data used in this demo can be accessed here: [Yelp Dataset](https://www.yelp.com/dataset/challenge)


## Building the SageMaker Endpoint
Follow along in the ``sage_maker_demo.ipynb`` notebook.

## Building the API
Follow this excellent [tutorial](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/) to setup the API Gateway to invoke a Lambda function to call your endpoint. You can skip the section on deploying the SageMaker endpoint if you followed my notebook above.

Also, if you're following my example, you'll want to use the ``lambda_function.py`` that I've defined in this repo. This function takes the request from the API, formats it in a way that makes sense to the model endpoint, calls the endpoint, and formats the response.
