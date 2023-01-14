from config.s3bucketConfig import *
from config.s3Connection import s3_connection
import random
s3 = s3_connection()


def post_image(file):
    file.name = str(random.random())

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


def delete_image(img_name):
    return s3.Object('buyself', 'detectimage/'+img_name).delete()
