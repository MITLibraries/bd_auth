import logging
import os

from flask import Flask, redirect
from flask_talisman import Talisman

from bdauth import auth, debug, openurl

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

if os.getenv('SENTRY_DSN'):
    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[FlaskIntegration()],
    )

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(auth.bp)
app.register_blueprint(debug.bp)
app.register_blueprint(openurl.bp)
Talisman(app)

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
    return redirect('https://libraries.mit.edu/borrow/borrowdirect/', 307)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
