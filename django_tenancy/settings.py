from pathlib import Path
import datetime
from django.contrib import messages
import logging
import os
from datetime import timedelta

#Basic config for logging add logging.info(f"string{}") in your code to log to the file

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logfile = f"logs/server_{timestamp}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filename=logfile,  # Log to this file
    filemode='a' 
)

DEBUG = os.environ.get('DEBUG', 0)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "'django-insecure-%ge(+b5+_0_8n2z6swm_v&xao0n+@gbj+sw#)o7hxqyy@7s52('"
)


ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.fusehub.imperisoft.co.uk', "https://fusehub.imperisoft.co.uk"]
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend'
]


INSTALLED_APPS = [
    "daphne",
    "channels",
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'apps.admin.realms',
    'apps.core.todo',
    'apps.core.timeline',
    
]

MIDDLEWARE = [
    'apps.admin.tenancy.middleware.domainrequest.DomainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

#channels 
ASGI_APPLICATION = "django_tenancy.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("django-tenancy-redis", 6379)], # use redis container name
        },
    },
}


ROOT_URLCONF = 'django_tenancy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'html_templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django-tenancy.wsgi.application'

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "django_tenancy"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-gmt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static/images")
STATICFILES_DIRS = [BASE_DIR / "static",]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# messages settings - these are bootsrap 4 alert css - https://getbootstrap.com/docs/4.0/components/alerts/
MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# api settings
GRAPHENE = {
    "SCHEMA": "django_tenancy.schema.schema"
}
GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=720),  # 1 hour
}

# multitenant settings

# domain you want to use for the management site 
MANAGEMENT_DOMAIN = os.environ.get('MANAGEMENT_DOMAIN', 'fusehub.imperisoft.co.uk')

USE_DJANGO_TEMPLATES = True

TRIAL_LENGTH = 30 # days

#logging for settings debug file in logs/server.log

logger = logging.getLogger(__name__)
logger.info(f"------------ Realm configuration ----------------")
logger.info(f" Management domain - https://{MANAGEMENT_DOMAIN} ")
logger.info(f"-------------------------------------------------")

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Realm panel",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Realms",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Realms",

    # Logo to use for your site, must be present in static files, used for brand on top left
     "site_logo": "images/Imperisoft.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "images/Imperisoft.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Django Realms",

    # Copyright on the footer
    "Open source project from": "Imperisoft",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    # "topmenu_links": [

    #     # Url that gets reversed (Permissions can be added)
    #     {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

    #     # external url that opens in a new window (Permissions can be added)
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

    #     # model admin to link to (Permissions checked against model)
    #     {"model": "auth.User"},

    #     # App with dropdown menu to all its models pages (Permissions checked against models)
    #     {"app": "books"},
    # ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "custom_css": "css/custom-jazzmin.css",

}