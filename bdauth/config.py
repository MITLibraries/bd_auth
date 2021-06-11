import os


class Config():
    DEBUG = os.getenv('FLASK_DEBUG', default=False)
    ENV = os.getenv('FLASK_ENV', default='production')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = 'testing'
