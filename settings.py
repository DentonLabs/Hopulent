# Django settings for Hopulent project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hopulent',                      # Or path to database file if using sqlite3.
        'USER': 'hopulent',                      # Not used with sqlite3.
        'PASSWORD': 'buddyholly',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/hopulent/webapps/static_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://hopulent.webfactional.com/media/'

STATIC_URL = '/static/'
	
EMAIL_HOST = 'smtp.webfactions.com'

EMAIL_HOST_USER = 'hopulent'

EMAIL_HOST_PASSWORD = 'buddyholly'

EMAIL_PORT = '25'

DEFAULT_FROM_EMAIL = 'hopulent@mail.webfaction.com'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://hopulent.webfactional.com/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ar+e(&ggk3si*rc8pb!@hm*d)$nzv-zpfkj&v%f)6lyf0bda_d'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hopulent.urls'

AUTH_PROFILE_MODULE = 'account.UserProfile'

TEMPLATE_DIRS = (
    '/home/hopulent/webapps/django/hopulent/templates',

     #Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
     #Always use forward slashes, even on Windows.
     #Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages', 
    'index',
    'browse',
    'beer',
    'brewery',
    'category',
    'style',
    'brewerygeocode',
    'review',
    'account',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'django.contrib.staticfiles',
)
