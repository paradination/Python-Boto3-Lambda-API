import boto3
s3 = boto3.client('s3')

response = s3.list_buckets()
print(response)

#uploading file to s3 bucket
print("\n")

bucket = "flossyezeudu"
file_path = 'C:\\Users\\chiag\\OneDrive\\Desktop\\Cloud DevOps\\Ag-devops\\Python\\python-introduction\\boto3-learning\\python-upload.txt'
mykey = "python_upload_test.txt"
with open(file_path, 'rb') as data:
    s3.upload_fileobj(data, bucket, mykey)

