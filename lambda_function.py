"""Function for Lambda to invoke SageMaker endpoint."""
import json
import os
import string

import boto3

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
RUNTIME = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    # Extract data for model.
    data = json.loads(json.dumps(event))
    model_data = data['data']
    print(model_data)
    # Preprocess data for model.
    if type(model_data) == str:
        model_data = clean_text(model_data)
    elif type(model_data) == list:
        model_data = [clean_text(text) for text in model_data]
    # Format payload for model api.
    payload = json.dumps({'instances': model_data})
    response = RUNTIME.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=payload)
    print(response)
    response = json.loads(response['Body'].read().decode())
    parsed_response = []
    for response_dict in response:
        if '__label__2' in response_dict['label']:
            parsed_response.append('positive')
        else:
            parsed_response.append('negative')
    return parsed_response


def clean_text(text):
    """Same as func in utils.py."""
    # Replace punctuation with whitespace.
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(translator)
    # Remove excess whitespace and return.
    return " ".join(text.split())
