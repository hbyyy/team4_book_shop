from .base import *

ALLOWED_HOSTS = ['web']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookmarket',
        'USER': os.environ.get('DB_USER', 'BOOKMARKET'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'BOOKMARKET1234'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': '10632',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'book-market-12345'
AWS_REGION = "ap-northeast-2"
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME