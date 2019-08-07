import json

from utils import make_response


def get_requried_params(event):
    try:
        org_id = event['queryStringParameters']['org_id']
        service_id = event['queryStringParameters']['service_id']
        user_id = event['queryStringParameters']['service_id']
    except Exception as e:
         raise e

    return org_id, service_id, user_id


def main(event, context):
    org_id, service_id, user_id = get_requried_params(event)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    return make_response(200,json.dumps(body))
