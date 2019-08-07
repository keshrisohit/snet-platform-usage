import json

from utils import make_response


def vlaidate_requried_params(event):
    try:
        body = json.loads(event['body'])
    except Exception as e:
        raise e
    return


def main(event, context):
    vlaidate_requried_params(event)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
