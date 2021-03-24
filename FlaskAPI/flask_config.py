import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # This secret is used for CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-should-be-a-secret'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    RESUMES_LOCATION = os.environ.get('RESUMES_LOCATION')  or "/var/www/kuse.com/kuse-resumes/"

    WEBSITE_EMAIL = os.environ.get('WEBSITE_EMAIL')

    WEBSITE_LINKEDIN = os.environ.get('WEBSITE_LINKEDIN')
    WEBSITE_FACEBOOK = os.environ.get('WEBSITE_FACEBOOK')
