import boto3
from Secret_manager import password, username
from config import Database

client = boto3.client('rds')

response = client.create_db_instance(
        AllocatedStorage=10,
        DBInstanceIdentifier=Database,
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername=username,
        MasterUserPassword=password,
        Port=3306
)

print (response)