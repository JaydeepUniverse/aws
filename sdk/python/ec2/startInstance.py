import boto3
client = boto3.client("ec2", region_name="us-east-2")
response = client.start_instances(
    InstanceIds=[
        'i-0c974222e9ae11487',
    ]
)