const { createApp } = Vue;

createApp({
    data() {
        return {
            features: [
                {
                    icon: 'fa-seedling',
                    title: 'Crop Monitoring',
                    description: 'Real-time tracking of crop health and growth stages using AI analysis'
                },
                {
                    icon: 'fa-bug',
                    title: 'Pest Detection', 
                    description: 'Early identification of pests and diseases with treatment recommendations'
                },
                {
                    icon: 'fa-tint',
                    title: 'Resource Optimization',
                    description: 'Smart water and fertilizer usage calculations for maximum yield'
                }
            ],
            activeTab: 'dashboard',
            currentLanguage: 'en',
            languages: [
                { code: 'en', 'name': 'English' },
                { code: 'hi', 'name': 'हिंदी' },
                { code: 'ta', 'name': 'தமிழ்' },
                { code: 'te', 'name': 'తెలుగు' },
                { code: 'kn', 'name': 'ಕನ್ನಡ' },
                { code: 'ml', 'name': 'മലയാളം' },
                { code: 'bn', 'name': 'বাংলা' },
                { code: 'mr', 'name': 'मराठी' },
                { code: 'gu', 'name': 'ગુજરાતી' },
                { code: 'pa', 'name': 'ਪੰਜਾਬੀ' },
                { code: 'or', 'name': 'ଓଡ଼ିଆ' }
            ],
            translations: {}
        }
    },
    methods: {
        changeTab(tab) {
            this.activeTab = tab;
        },
        changeLanguage(lang) {
            this.currentLanguage = lang;
            this.loadTranslations();
        },
        async loadTranslations() {
            try {
                const response = await fetch(`/translations/translate?text=all&target_lang=${this.currentLanguage}`);
                const data = await response.json();
                this.translations = data.translated_text;
                document.documentElement.lang = this.currentLanguage;
            } catch (error) {
                console.error('Error loading translations:', error);
            }
        },
        t(key) {
            return this.translations[key] || key;
        },
        async analyzeCropImage(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            const formData = new FormData();
            formData.append('image', file);
            
            try {
                const response = await fetch(`/api/analyze-crop?lang=${this.currentLanguage}`, {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                
                alert(`${this.t('Disease')}: ${result.disease}\n${this.t('Treatment')}: ${result.treatment}\n${this.t('Confidence')}: ${result.confidence}`);
            } catch (error) {
                console.error('Error analyzing image:', error);
                alert(this.t('Error analyzing image. Please try again.'));
            }
        }
    },
    mounted() {
        this.loadTranslations();
    }
}).mount('#app');