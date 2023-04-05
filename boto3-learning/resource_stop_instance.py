#session creation for current region
import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2 = session.resource('ec2')

#checking to see available instances
instance = ec2.instances.filter(
    Filters = [{'Name':'instance-state-name', 
                'Values': ['running']}]
    )
#stopping a running instance
for i in instance:
    i.stop()
    print("stopped", i.id)