
import boto3

def check_s3_bucket_list():
    print("this is to check all s3 bucket list on account")
    s3_resource = boto3.resource("s3")
    for buckets in s3_resource.buckets.all():
        print(buckets.name)