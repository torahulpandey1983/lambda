import boto3

client = boto3.client('ec2')
response=client.stop_instances(
    InstanceIds=['i-022e9e3f85ec1fa0c']
)

