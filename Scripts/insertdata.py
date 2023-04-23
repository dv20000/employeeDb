import boto3
import mysql.connector
from config import *
"""
db_conn = mysql.connector.connect(
    host=hostname,
    port=3306,
    user=username,
    password=password,
    database=Database

)
cursor=db_conn.cursor()"""
"""
create_table = """
#CREATE TABLE Employee (
#  emp_id VARCHAR(255) PRIMARY KEY,
#  first_name VARCHAR(255),
#  last_name VARCHAR(255),
#  pri_skill VARCHAR(255),
#  location VARCHAR(255)
#)"""

#cursor.execute(create_table)

#add_data = "INSERT INTO employees ( first_name, last_name, pri_skill, location) VALUES (%s, %s, %s, %s)"

#data = ('Rohini', 'Reddy', 'Python', 'kansas')
#çdata = ('Medha', 'Reddy', 'SQL', 'India')

#emp_id = 1 

#select_sql = "SELECT * FROM employees where emp_id = %s"

#response =cursor.execute(select_sql , (emp_id))

#print(response)

# Execute the SQL statement to insert the data
#cursor.execute(add_data, data)

# Commit the changes
#db_conn.commit()

# Close the cursor and connection
#cursor.close()
#db_conn.close()

"""
cursor = db_conn.cursor()

# define the employee ID value
emp_id = 2

# execute the SELECT query with the employee ID value as a parameter
query = "SELECT * FROM employees WHERE emp_id = %s"
cursor.execute(query, (emp_id,))

myresult = cursor.fetchall()

print(myresult)



# close the cursor and database connection
cursor.close()
db_conn.close() """