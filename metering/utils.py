import logging


def make_response(status_code, body):
    return {
        "statusCode": status_code,
        "body": body
    }

# def configure_log(logger):
#
#     logger.setLevel(logging.INFO)
#
#     # create a file handler
#     handler = logging.
#     handler.setLevel(logging.INFO)
#
#     # create a logging format
#     formatter = logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(formatter)
#
#     # add the handlers to the logger
#     logger.addHandler(handler)
