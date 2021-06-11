import os


class Config():
    DEBUG = os.getenv('FLASK_DEBUG', default=False)
    ENV = os.getenv('FLASK_ENV', default='production')
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'devsecrets'


class TestingConfig(Config):
    TESTING = True

    DEBUG = True
    ENV = 'testing'
    SECRET_KEY = 'testing'
