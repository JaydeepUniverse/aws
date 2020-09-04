import boto3

client = boto3.client('iam')
listOfUsers = client.list_users()

for i in listOfUsers['Users']:
    for j in client.list_attached_user_policies(UserName=i['UserName'])['AttachedPolicies']:
        if j['PolicyName'] == 'AdministratorAccess':
            print (i['UserName'])
