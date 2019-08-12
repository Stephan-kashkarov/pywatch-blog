import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ORIGINS = ["*"]
    SECRET_KEY = 'KEY!!'


class Development(Config):
    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Testing(Config):
    PORT = 5000
    DEBUG = False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ELASTICSEARCH_URL = None


class Production(Config):
    PORT = 5000
    Testing = False
    Debug = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'dev': Development,
    'prod': Production,
    'test': Testing,
}
