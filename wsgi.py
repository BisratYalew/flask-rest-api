import os

from flask_rest_app.application import create_app


env = os.environ.get('APP_ENV')

if not env:
    raise Exception('APP_ENV can not be found')

application = create_app(env)
