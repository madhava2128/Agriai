from flask import Blueprint, request, jsonify, current_app
from app.services.ai_services import analyze_crop_image, get_crop_recommendations
from app.services.translation_service import translate_text
import os

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/analyze-crop', methods=['POST'])
def analyze_crop():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    lang = request.args.get('lang', 'en')
    
    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400
    
    if image and allowed_file(image.filename):
        try:
            filename = os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename)
            image.save(filename)
            
            result = analyze_crop_image(filename)
            
            if lang != 'en':
                result['disease'] = translate_text(result['disease'], lang)
                result['treatment'] = translate_text(result['treatment'], lang)
                result['confidence'] = translate_text(f"{result['confidence']:.2f}% confidence", lang)
            
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            if os.path.exists(filename):
                os.remove(filename)
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@api_blueprint.route('/crop-recommendations', methods=['GET'])
def crop_recommendations():
    soil_type = request.args.get('soil_type')
    climate = request.args.get('climate')
    season = request.args.get('season')
    lang = request.args.get('lang', 'en')
    
    try:
        recommendations = get_crop_recommendations(soil_type, climate, season)
        
        if lang != 'en':
            recommendations = [translate_text(r, lang) for r in recommendations]
            
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']