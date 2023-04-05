# TASK: creating AMI from instances different by filters (Env = Prod/Dev)


#session creation for current region
import boto3
import time

session = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2 = session.client('ec2')

#getting the list of available instances

all_instances = ec2.describe_instances()
for i in all_instances["Reservations"]:
    for j in i["Instances"]:
        print("instanceID", j["InstanceId"], "ImageID", j["ImageId"], "Tags", j["Tags"] )







#getting image on particular instance via filter eg Env = Prod and copying image to another region
instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'Env',
            'Values': [
                'Prod',
            ]
        },
    ]
)
for i in instances["Reservations"]:
    for j in i["Instances"]:
        print("instanceID", j["InstanceId"], "ImageID", j["ImageId"], "Tags", j["Tags"] )
        response = ec2.create_image(
            InstanceId=j["InstanceId"],
            Name=j["Tags"][0]['Value']
        )
        print(response)
        #name of the region will be destination region we will prefer
        session_dest = boto3.session.Session(profile_name="default", region_name="us-east-2")
        image_dest = session_dest.client('ec2')

        time.sleep(120)

        copy_response = image_dest.copy_image(
            SourceImageId= response['ImageId'],
            SourceRegion='us-east-1',
            Name=j["Tags"][0]['Value']
        )




#creating image: for ansible tower
response_ansible = ec2.create_image(
            InstanceId='i-085b13c09e20001c9',
            Name='Ansible_Tower_Image_on_Centos'
        )
print(response_ansible)


#Copy image from one region to another, session created for that
#session creation for destination region via copy
session_dest = boto3.session.Session(profile_name="default", region_name="us-east-2")
image_dest = session_dest.client('ec2')

copy_response = image_dest.copy_image(
    SourceImageId='ami-026711d10a862a7e9',
    SourceRegion='us-east-1',
    Name="Images to copy"
)
print(copy_response)