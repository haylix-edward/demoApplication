import json

def lambda_handler(event, context):
    try:
        body = {
            "answer": event["a"] + event["b"]
        }
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type" : "application/json"
            },
            "body": body
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type" : "application/json"
            },
            "body": json.dumps(e.message)
        }

