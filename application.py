import boto3 
import mysql.connector
from flask import Flask,render_template,request
from Secret_manager import password, username
from config import *

app = Flask(__name__)

db_conn = mysql.connector.connect(
    host=hostname,
    port=3306,
    user=username,
    password=password,
    database=Database)

cursor=db_conn.cursor()

#output = {}
#table = Tablename
#bucket= bucketname


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/addemployee", methods=['GET','POST'])
def AddEmployee():
    return render_template('AddEmp.html')

  
@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    add_data = "INSERT INTO employees ( emp_id ,first_name, last_name, pri_skill, location) VALUES (%s, %s, %s, %s, %s)"

    data = (emp_id, first_name, last_name, pri_skill, location)
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:

        cursor.execute(add_data, data)
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name
        # Uplaod image file in S3 #
        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
        s3 = boto3.resource('s3')
        try:
            print("Data inserted in MySQL RDS... uploading image to S3...")
            s3.Bucket(bucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)
            bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket)
            s3_location = (bucket_location['LocationConstraint'])

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                bucket,
                emp_image_file_name_in_s3)

        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)

@app.route("/getemployee", methods=['GET','POST'])
def GetEmployee():
    return render_template('GetEmp.html')

@app.route("/fetchdata", methods=['POST'])
def GetEmp():
    cursor = db_conn.cursor()
    emp_id = request.form['emp_id']
    query = "SELECT * FROM employees WHERE emp_id = %s"

    try:
        cursor.execute(query, (emp_id,))
        myresult = cursor.fetchall()
        print(myresult)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
    return render_template('GetEmpOutput.html',name = myresult)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
