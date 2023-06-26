
import boto3

def db_handler(event, context):
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
        'message': 'DynamoDB table populated successfully'
    }

    return {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': message
    }