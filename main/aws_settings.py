# main/aws_settings.py
#import os

#AWS_QUERYSTRING_AUTH = False
#AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
#AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
#MEDIA_URL = 'http://%s.s3.amazonaws.com/your-folder/' % AWS_STORAGE_BUCKET_NAME
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400',
#}

#STATICFILES_STORAGE = 'myproject.storage.S3Storage'

STATIC_URL = 'https://s3.eu-central-1.amazonaws.com/aws-django-docker-static/'
