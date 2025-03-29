from flask import Flask
from config import config
from flask_cors import CORS

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    CORS(app)
    
    from .routes.api import api_blueprint
    from .routes.translations import translations_blueprint
    
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(translations_blueprint, url_prefix='/translations')
    
    return app