import boto3
iam = boto3.resource("iam")

policy_iterator = iam.policies.all()

for p in policy_iterator:
    if p.policy_name == "PowerUserAccess":
        print(p.policy_name, p.create_date, p.policy_id)
        p.attach_user(
            UserName = "ag-paradin",
        )