import json
import os
from flask import current_app
from pathlib import Path
from googletrans import Translator

translations = {}
for lang in current_app.config['SUPPORTED_LANGUAGES']:
    try:
        trans_path = Path(current_app.root_path) / 'static' / 'translations' / f'{lang}.json'
        with open(trans_path, 'r', encoding='utf-8') as f:
            translations[lang] = json.load(f)
    except Exception as e:
        print(f"Error loading {lang} translations: {e}")

def get_translation(text, target_lang='en'):
    if target_lang not in current_app.config['SUPPORTED_LANGUAGES']:
        target_lang = current_app.config['DEFAULT_LANGUAGE']
    
    for key, value in translations[target_lang].items():
        if key.lower() == text.lower():
            return value
    
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except:
        return text

def translate_text(text, target_lang='en'):
    return get_translation(text, target_lang)

def get_supported_languages():
    return [
        {'code': 'en', 'name': 'English'},
        {'code': 'hi', 'name': 'हिंदी'},
        {'code': 'ta', 'name': 'தமிழ்'},
        {'code': 'te', 'name': 'తెలుగు'},
        {'code': 'kn', 'name': 'ಕನ್ನಡ'},
        {'code': 'ml', 'name': 'മലയാളം'},
        {'code': 'bn', 'name': 'বাংলা'},
        {'code': 'mr', 'name': 'मराठी'},
        {'code': 'gu', 'name': 'ગુજરાતી'},
        {'code': 'pa', 'name': 'ਪੰਜਾਬੀ'},
        {'code': 'or', 'name': 'ଓଡ଼ିଆ'}
    ]