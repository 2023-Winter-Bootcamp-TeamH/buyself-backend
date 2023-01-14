import boto3
from botocore.client import Config

from .s3bucketConfig import ACCESS_KEY_ID, SECRET_ACCESS_KEY

def s3_connection():
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4'))
    return s3