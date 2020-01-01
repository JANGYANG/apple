ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = { 
    'default': 
    { 'ENGINE': 'django.db.backends.postgresql', 
    'NAME': 'manitto_apple', 
    'USER': 'jyct', 
    'PASSWORD': 'abcd', 
    'HOST': '127.0.0.1', 
    'PORT': '5432', 
    } }

DEBUG = False