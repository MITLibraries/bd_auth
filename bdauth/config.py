import os


class Config():
    DEBUG = os.getenv('FLASK_DEBUG', default=False)
    ENV = os.getenv('FLASK_ENV', default='production')
    SECRET_KEY = os.getenv('SECRET_KEY')
    BD_KEY = os.getenv('BD_KEY')
    BD_URL = os.getenv('BD_URL')
    URN_UID = os.getenv('URN_UID')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'devsecrets'
    BD_KEY = os.getenv('BD_KEY')
    BD_URL = os.getenv('BD_URL')
    FAKE_USER = os.getenv('FAKE_USER')


class TestingConfig(Config):
    TESTING = True

    DEBUG = True
    ENV = 'testing'
    SECRET_KEY = 'testing'
    BD_URL = 'http://example.com/?LS=XYZ'
    FAKE_USER = 'yo@example.com'
