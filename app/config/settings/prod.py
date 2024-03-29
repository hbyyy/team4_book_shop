from .base import *

print('-------------prod-----------------')
ALLOWED_HOSTS = ['web']
DEBUG = True
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
AWS_DEFAULT_ACL = 'private'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'book-rental-123'
