
#lambda function put item
import boto3
session = session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('paradin-clients')

def lambda_handler(event, context):
    response = table.put_item(
        Item ={
            "ClientID": "1112",
            "ClientName": "jay",
            "Department": "5",
            "Age":"30"
        }
    )

    print("the views of added items:", response)


#For API gateway put item

import boto3
import json

session = session = boto3.session.Session(region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('paradin-clients')

def lambda_handler(event, context):
    print(event["body"])

    response = table.put_item(
        Item = json.loads(event["body"])
    )
    response_output = json.loads(event["body"])
    
    return{
        "statusCode": 200,
        "body": json.dumps(response_output)
    }