import boto3
ec2=boto3.client('ec2')
response=ec2.run_instances(
    ImageId='ami-084568db4383264d4',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    
)
print(response['Instances'][0]['InstanceId'])

  