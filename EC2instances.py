import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances (InstanceIds=['i-0f78f117c99810cbf', 'i-0cca3f6af2acb19ed', 'i-08a4d5eac093f1b67'])

print(response)