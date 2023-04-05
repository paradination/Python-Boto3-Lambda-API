#this will send SNS onces an update is made on the dynamodb
import boto3
import json

session = session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
client = session.client('sns')

table = dynamodb.Table('paradin-clients')
client = session.client('sns')


def lambda_handler(event, context):
    response = table.scan(
        TableName='paradin-clients',
        Select='ALL_ATTRIBUTES'
    )
    
    print(event)

    print(response["Items"])
    #sns notification from the event
    response_sns = client.publish(
        TopicArn='arn:aws:sns:us-east-1:925229124194:Paradin-DynamoDB-Topic',
        Message=str({
            "message": "A new update was made on dynamodb",
            "old_change": event["Records"][0]["dynamodb"]["OldImage"],
            "new_change": event["Records"][0]["dynamodb"]["NewImage"],
            "updated_database_to":response["Items"]
            }
        ),
        Subject='update on dynamodb table'
    )
    print(response_sns)
    
    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"])
    }




