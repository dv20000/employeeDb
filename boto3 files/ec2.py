import boto3
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
        ImageId='ami-02396cdd13e9a1257',
        key_name = 'test-pair' ,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
)

print(instance)