import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SUPPORTED_LANGUAGES = ['en', 'hi', 'ta', 'te', 'kn', 'ml', 'bn', 'mr', 'gu', 'pa', 'or']
    DEFAULT_LANGUAGE = 'en'
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/plant_disease_model.h5')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}