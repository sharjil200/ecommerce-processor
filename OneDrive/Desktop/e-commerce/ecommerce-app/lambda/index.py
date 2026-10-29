import json

def handler(event, context):
    print("Processing E-commerce Order Event:", json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Payment processed successfully!'})
    }