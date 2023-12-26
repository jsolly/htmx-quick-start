def lambda_handler(event, context):
    return {
        'headers': {'content-type': 'text/html'},
        'statusCode': 200,
        'body': "<li><input type='checkbox'>New todo from Amz Lambda!</li>"
    }