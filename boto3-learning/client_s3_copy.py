#copy object from source to destination

import boto3
session = boto3.session.Session(profile_name="default", region_name="us-east-1")

client = session.client('s3')

bucket_objects = client.list_objects_v2(
    Bucket='flossyezeudu',
)

for i in bucket_objects["Contents"]:
    print(i['Key'])
    files = i['Key']
    #copying a particular content and not entire contents in a bucket
    if files == "python_upload_test.txt":
        object_copy = client.copy_object(
            Bucket='ag-sanitycheck01',
            CopySource='flossyezeudu/' + files ,
            Key=files
        )
        print(object_copy)

    #copy all contents into another bucket
    # Object_copy_all = client.copy_object(
    #     Bucket='ag-sanitycheck01',
    #     CopySource='flossyezeudu' + i['Key'],
    #     Key=i['Key']
    # )
    # print(Object_copy_all)


