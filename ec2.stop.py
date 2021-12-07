import boto3


client = boto3.client('ec2')
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ["demo-instance"]

        }
    ]

)

for r in response['Reservations']:
  for i in r['Instances']:
     instance = client.stop_instances(InstanceIds=[i['InstanceId']])
     print("stopped successfully \n ", i['InstanceId'])


