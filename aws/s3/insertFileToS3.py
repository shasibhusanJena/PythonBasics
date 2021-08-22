import boto
from boto.exception import S3ResponseError
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
END_POINT = 'Global'                          # eg. us-east-1
S3_HOST = 's3.ap-south-1.amazonaws.com'                            # eg. s3.us-east-1.amazonaws.com
BUCKET_NAME = 'shasi-s3-bucket'
FILENAME = 'upload.txt'
UPLOADED_FILENAME = 'dumps/upload.txt'
# include folders in file path. If it doesn't exist, it will be created

s3 = boto.s3.connect_to_region(END_POINT,
                           aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                           host=S3_HOST)

while True:
    try:
        bucket = s3.get_bucket(BUCKET_NAME)
        break
    except S3ResponseError:
        print("error occur while handling value")
    except(RuntimeError,TypeError,NameError):
        pass


k = Key(bucket)
k.key = UPLOADED_FILENAME
k.set_contents_from_filename(FILENAME)

