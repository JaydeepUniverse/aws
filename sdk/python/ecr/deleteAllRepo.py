## Do AWS CLI configuration - aws configure

## If want to delete irrespective of repositories contains images or not then use this command
## client.delete_repository(repositoryName=i['repositoryName'], force=True)

import boto3
client = boto3.client("ecr")
registryList = client.describe_repositories()

for i in registryList["repositories"]:
    print(i['repositoryName'])
    client.delete_repository(repositoryName=i['repositoryName'])
