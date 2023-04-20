import boto3
import json

client = boto3.client('secretsmanager')

def createSecret():
    response = client.create_secret(
        Name='TestDBsecret',
        SecretString='{"username": "root", "password": "employee123"}'
    )
    return response

def fetchSecret():
    response = client.get_secret_value(
    SecretId='TestDBsecret'
    )
    database_secrets = json.loads(response['SecretString'])
    return database_secrets['username']

def fetchSecret1():
    response = client.get_secret_value(
    SecretId='TestDBsecret'
    )
    database_secrets = json.loads(response['SecretString'])
    return database_secrets['password']

#createresp = createSecret()
#print(createresp)

username = fetchSecret()
print(username)

password = fetchSecret1()
print(password)

