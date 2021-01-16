import boto3
client = boto3.client("ec2", region_name="us-east-2")
response = client.describe_instances(
    InstanceIds=[
        'i-0c974222e9ae11487',
    ]
)

print (response["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["Association"]["PublicIp"])