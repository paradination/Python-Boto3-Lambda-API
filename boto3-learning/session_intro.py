import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

ec2 = session.client('ec2')

response = ec2.run_instances(
    #insert into there about creation of ec2 via documentation


)
print(response)

