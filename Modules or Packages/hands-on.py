import uuid
import os


print(uuid.uuid4())

print(os.getcwd())

from aws_essentials import s3

s3.check_s3_bucket_list()