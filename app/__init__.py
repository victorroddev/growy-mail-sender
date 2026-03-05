from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from config import config

mail = Mail()

def create_app(env='production'):
    app = Flask(__name__)
    app.config.from_object(config[env])

    mail.init_app(app)
    CORS(app, origins=app.config['ALLOWED_ORIGINS'])

    from .routes import bp
    app.register_blueprint(bp, url_prefix='/api')

    return app