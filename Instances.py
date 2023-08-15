import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances (InstanceIds=['i-05af0ad76b030c773', 'i-0d2aa2eb429cbd948', 'i-029dd5e0f53055fb7'])

print(response)
