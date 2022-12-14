# app/__init__.py

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#instantiate the extensions
db = SQLAlchemy()
cors = CORS()

def create_app(script_info=None):
    
    #instantiate the app
    app = Flask(__name__)

    #set config

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    #set up extensions
    db.init_app(app)
    cors.init_app(app,resources={r"*":{"origins":"*"}})

    #register api
    from app.api import api
    
    api.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app":app,"db":db}
    
    return app
