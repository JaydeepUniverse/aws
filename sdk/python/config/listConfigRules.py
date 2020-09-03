## Do AWS CLI configuration - aws configure

import boto3
client = boto3.client('config')
rulesList = client.describe_config_rules()
for i in rulesList['ConfigRules']:
    print(i['ConfigRuleName'])
