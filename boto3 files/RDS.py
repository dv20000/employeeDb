
import boto3
import mysql.connector

client = boto3.client('rds')
"""
response = client.create_db_instance(
        AllocatedStorage=10,
        DBInstanceIdentifier=Database,
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername='root',
        MasterUserPassword='employee123',
        Port=3306
)

print (response)
"""

db_conn = mysql.connector.connect(
    host='empdatabase.cjqjmoxodmld.us-east-1.rds.amazonaws.com',
    port=3306,
    user='root',
    password='employee123',
)

cursor=db_conn.cursor()

create_db_command = "CREATE DATABASE empDB;"

# Execute the SQL command to create the database
cursor.execute(create_db_command)
"""
create_table = """
#CREATE TABLE Employee (
#  emp_id VARCHAR(255) PRIMARY KEY,
#  first_name VARCHAR(255),
# last_name VARCHAR(255),
#  pri_skill VARCHAR(255),
#  Company VARCHAR(255)
#)"""
"""
cursor.execute(create_table)

# Commit the changes
db_conn.commit()"""

# Close the cursor and connection
cursor.close()
db_conn.close() 