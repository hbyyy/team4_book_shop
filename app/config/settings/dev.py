from .base import *

print('--------------dev----------------')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
ALLOWED_HOSTS = ['*']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite3.db')
    }
}