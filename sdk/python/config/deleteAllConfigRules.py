## Do AWS CLI configuration - aws configure

## At a time list only gives 26 number of rules, so to delete them all run this script multiple times or 
## create new script which can loop everytime until all rules will be deleted

import boto3
client = boto3.client('config')
rulesList = client.describe_config_rules()
n=1
for i in rulesList['ConfigRules']:
    print(i['ConfigRuleName'])
    client.delete_config_rule(ConfigRuleName=i['ConfigRuleName'])
    n=n+1
    print(n)
