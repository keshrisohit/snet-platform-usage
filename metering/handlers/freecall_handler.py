import json

from metering.utils import make_response


def get_requried_params(event):
    try:
        org_id = event['queryStringParameters']['org_id']
        service_id = event['queryStringParameters']['service_id']
        user_id = event['queryStringParameters']['service_id']
    except Exception as e:

        make_response(400, "Please pass required parameters org_id, service_id ,user_id")

    return org_id, service_id, user_id


def hello(event, context):
    org_id, service_id, user_id = get_requried_params(event)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
