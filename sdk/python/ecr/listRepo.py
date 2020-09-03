## Do AWS CLI configuration - aws configure

import boto3
client = boto3.client("ecr")
registryList = client.describe_repositories()

for i in registryList["repositories"]:
    print(i['repositoryName'])
