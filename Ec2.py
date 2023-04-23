import boto3

# Define EC2 client
ec2 = boto3.client('ec2')

# Define instance parameters
image_id = 'ami-0c94855ba95c71c99'  # Amazon Linux 2 AMI (HVM), SSD Volume Type
instance_type = 't2.micro'
key_name = 'my-ec2-key'
subnet_id = 'subnet-123456'
security_group_ids = ['sg-123456']

# Create the EC2 instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SubnetId=subnet_id,
    SecurityGroupIds=security_group_ids,
    MaxCount=1,
    MinCount=1,
    InstanceInitiatedShutdownBehavior='terminate'
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']

# Print the instance ID
print(f'EC2 instance created with ID: {instance_id}')