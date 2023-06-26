import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test_table_example')

    items = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]

    for item in items:
        table.put_item(Item=item)
    message = {
        'message': 'Execution started successfully! DB also'
    }
    return json.dumps({
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': message
    })