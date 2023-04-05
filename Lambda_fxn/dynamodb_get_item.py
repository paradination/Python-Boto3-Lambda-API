import boto3
import json

session = session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('paradin-clients')

def lambda_handler(event, context):
    response = table.get_item(
        Key ={
            "ClientID": "1122331",
            "ClientName": "Ag"

        }
    )

    print("the views of added items:", response)

#get with API calls

import boto3
import json

session = session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('paradin-clients')

def lambda_handler(event, context):

    response = table.get_item(
        Key = event["queryStringParameters"]
    )
    print(response["Item"])
    return{
        "statusCode": 200,
        "body": json.dumps(response["Item"])
    }