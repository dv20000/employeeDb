import boto3
from Secret_manager import password, username
from config import *
import mysql.connector
from config import Database

"""
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

print (response)"""

db_conn = mysql.connector.connect(
    host=hostname,
    port=3306,
    user=username,
    password=password,
    database=Database
)

cursor=db_conn.cursor()

#create_db_command = "CREATE DATABASE Empdatabase;"

# Execute the SQL command to create the database
#cursor.execute(create_db_command)

create_table = """
CREATE TABLE Employee (
  emp_id VARCHAR(255) PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  pri_skill VARCHAR(255),
  Company VARCHAR(255)
)"""

cursor.execute(create_table)

# Commit the changes
db_conn.commit()

# Close the cursor and connection
cursor.close()
db_conn.close()