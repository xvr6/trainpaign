from flask import Flask
from flask_session import Session
from config import Config
from app.controller.routes import routes_blueprint as routes

# extensions
session = Session()

def create_app(config_class = Config):
    # app init
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER

    session.init_app(app)

    # blueprint registration
    app.register_blueprint(routes)

    return app