import os
from flask import Flask


def create_app(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)
    print(f'created app with config: {config}')

    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import api
    app.register_blueprint(api.bp)

    return app
