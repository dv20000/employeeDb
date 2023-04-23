import boto3
from config import bucketname

bucket = boto3.client('s3')

response = bucket.create_bucket(
    Bucket=bucketname,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1' # Replace with your desired region
    }
)
image_path = '/Users/rohini14/Documents/aws/project/images/Rohini.jpeg'
object_key = 'images/Rohini.jpg'
bucket.upload_file(image_path, bucketname, object_key)