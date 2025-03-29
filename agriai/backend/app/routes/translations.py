from flask import Blueprint, request, jsonify
from app.services.translation_service import get_supported_languages

translations_blueprint = Blueprint('translations', __name__)

@translations_blueprint.route('/supported-languages', methods=['GET'])
def supported_languages():
    languages = get_supported_languages()
    return jsonify({'languages': languages})

@translations_blueprint.route('/translate', methods=['GET'])
def translate():
    text = request.args.get('text')
    target_lang = request.args.get('target_lang', 'en')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        translated_text = get_translation(text, target_lang)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500