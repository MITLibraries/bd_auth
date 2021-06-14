import logging
import os

from flask import Flask

from bdauth import auth, debug
from bdauth.auth import login_required

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(auth.bp)
app.register_blueprint(debug.bp)

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
