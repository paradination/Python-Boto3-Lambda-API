#removed unused volumes


#session creation for current region
import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2 = session.client('ec2')

volumes = ec2.describe_volumes(
    Filters=[
                {
                    'Name': 'status',
                    'Values': [
                        'available',
                    ]
                },
            ]
)

print(volumes["Volumes"])

print("\nthe specific available volume id")
for i in volumes["Volumes"]:
    print("curent EBS volume:", i["VolumeId"])
    #deleting the volumes
    response = ec2.delete_volume(
    VolumeId=i["VolumeId"],
)
print("volume delete display", response)
