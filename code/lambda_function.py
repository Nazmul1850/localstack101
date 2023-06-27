import json


def lambda_handler(event, context):
    message = {
        'message': 'Execution started successfully!'
    }
    return {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': message
    }