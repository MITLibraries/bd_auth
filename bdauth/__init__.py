import logging
import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

flask_env = os.getenv('FLASK_ENV')

if flask_env == 'development':
    app.config.from_object('bdauth.config.DevelopmentConfig')
elif flask_env == 'production':
    app.config.from_object('bdauth.config.Config')
else:
    app.config.from_object('bdauth.config.TestingConfig')


logging.basicConfig(level=logging.INFO)


@app.route('/')
def root():
    return 'Hallo!'


@app.route('/ping')
def ping():
    return 'pong'
