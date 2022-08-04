from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'azerty'

    from .auth import auth
    from .application import application

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(application, url_prefix='/')


    return app