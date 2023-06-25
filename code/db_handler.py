import json


def db_handler(event, context):
    message = {
        'message': 'Execution started successfully From DB Handler!'
    }
    return {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': message
    }