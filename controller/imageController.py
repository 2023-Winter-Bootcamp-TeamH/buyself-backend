import requests
from io import BytesIO
from PIL import Image

from config.s3Config import *
from config.s3Connection import s3_connection

s3 = s3_connection()

def post_image(file):
    file.name = file.filename

    s3.Bucket(S3_BUCKET_NAME).put_object(
        Body=file,
        Key='detectimage/' + file.name,
        ContentType='image/jpeg'
    )
    img_name = ('%s' % file.name)
    return img_name

def get_url(img_name):

    url = f"https://{S3_BUCKET_NAME}.s3.{S3_BUCKET_REGION}.amazonaws.com/detectimage/{img_name}"

    return url

def use_url(img_name):
    url = get_url(img_name)

    res = requests.get(url)

    img = Image.open(BytesIO(res.content))