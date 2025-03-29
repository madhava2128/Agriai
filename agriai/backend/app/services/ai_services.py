import numpy as np
from PIL import Image

class MockCropDiseaseModel:
    def __init__(self):
        self.class_names = ['Healthy', 'Powdery Mildew', 'Leaf Rust', 'Bacterial Blight']
        self.treatments = {
            'Healthy': 'No treatment needed. Continue good farming practices.',
            'Powdery Mildew': 'Apply sulfur or potassium bicarbonate treatments.',
            'Leaf Rust': 'Use fungicides containing propiconazole or tebuconazole.',
            'Bacterial Blight': 'Apply copper-based bactericides and remove infected plants.'
        }
    
    def predict(self, image):
        pred_class = np.random.choice(self.class_names, p=[0.3, 0.2, 0.3, 0.2])
        confidence = np.random.uniform(0.7, 0.95)
        return pred_class, confidence

model = MockCropDiseaseModel()

def analyze_crop_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((256, 256))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        pred_class, confidence = model.predict(img_array)
        
        return {
            'status': 'success',
            'disease': pred_class,
            'treatment': model.treatments[pred_class],
            'confidence': float(confidence)
        }
    except Exception as e:
        raise e

def get_crop_recommendations(soil_type, climate, season):
    recommendations = {
        'clay': {
            'tropical': {
                'summer': ['Rice', 'Sugarcane', 'Banana'],
                'winter': ['Wheat', 'Barley', 'Mustard']
            },
            'temperate': {
                'summer': ['Corn', 'Soybean', 'Sunflower'],
                'winter': ['Wheat', 'Oats', 'Canola']
            }
        },
        'sandy': {
            'tropical': {
                'summer': ['Groundnut', 'Pearl Millet', 'Sorghum'],
                'winter': ['Chickpea', 'Lentil', 'Mustard']
            },
            'temperate': {
                'summer': ['Potato', 'Carrot', 'Radish'],
                'winter': ['Rye', 'Winter Peas', 'Fava Beans']
            }
        }
    }
    
    default_rec = ['Maize', 'Beans', 'Potatoes', 'Tomatoes']
    
    try:
        return recommendations.get(soil_type, {}).get(climate, {}).get(season, default_rec)
    except:
        return default_rec