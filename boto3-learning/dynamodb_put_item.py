import boto3
session = session = boto3.session.Session(profile_name="default", region_name="us-east-1")
dynamodb = session.resource('dynamodb')

table = dynamodb.Table('paradin-clients')

response = table.put_item(
    Item ={
        "ClientID": "1112",
        "ClientName": "jay",
        "Department": "5",
        "Age":"30"
    }
)

print("the views of added items:", response)