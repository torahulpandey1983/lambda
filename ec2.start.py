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
     instance = client.start_instances(InstanceIds=[i['InstanceId']])
     print("started successfully \n ", i['InstanceId'])


'''
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-022e9e3f85ec1fa0c')

result = instance.start()
print(result)

'''



