# Agriai Project

Agriai is a web application designed to facilitate multilingual translation services using AI technologies. The project is structured into two main components: the backend and the frontend.

## Project Structure

```
agriai/
├── backend/                  # Backend application
│   ├── app/                  # Application package
│   │   ├── __init__.py       # Initializes the app package
│   │   ├── routes/           # Contains route definitions
│   │   │   ├── __init__.py   # Initializes the routes package
│   │   │   ├── api.py        # API route handlers
│   │   │   └── translations.py # Translation-related routes
│   │   ├── services/         # Contains service definitions
│   │   │   ├── __init__.py   # Initializes the services package
│   │   │   ├── ai_services.py # AI-related services
│   │   │   └── translation_service.py # Translation services
│   │   ├── models/           # Contains data models
│   │   │   ├── __init__.py   # Initializes the models package
│   │   │   └── schemas.py     # Data schemas
│   │   └── static/           # Static files
│   │       └── translations/  # Translation files
│   │           ├── en.json    # English translations
│   │           ├── hi.json    # Hindi translations
│   │           ├── ta.json    # Tamil translations
│   │           ├── te.json    # Telugu translations
│   │           ├── kn.json    # Kannada translations
│   │           ├── ml.json    # Malayalam translations
│   │           ├── bn.json    # Bengali translations
│   │           ├── mr.json    # Marathi translations
│   │           ├── gu.json    # Gujarati translations
│   │           ├── pa.json    # Punjabi translations
│   │           └── or.json    # Odia translations
│   ├── config.py              # Configuration settings
│   ├── requirements.txt        # Backend dependencies
│   └── server.py              # Entry point for the backend
│
├── frontend/                 # Frontend application
│   ├── public/               # Public assets
│   │   ├── index.html        # Main HTML file
│   │   ├── favicon.ico       # Favicon
│   │   └── assets/           # Additional assets
│   │       ├── logo.png      # Logo image
│   │       └── images/       # Additional images
│   ├── src/                  # Source files
│   │   ├── assets/           # Assets for the frontend
│   │   │   ├── css/          # CSS files
│   │   │   │   └── main.css   # Main CSS styles
│   │   │   └── js/           # JavaScript files
│   │   │       └── app.js    # Main JavaScript logic
│   │   ├── components/       # Vue components
│   │   │   ├── LanguageSelector.vue # Language selection component
│   │   │   ├── FeatureCard.vue      # Feature card component
│   │   │   └── DashboardPanel.vue    # Dashboard panel component
│   │   └── views/            # Vue views
│   │       ├── HomeView.vue  # Home view
│   │       ├── FeaturesView.vue # Features view
│   │       └── DashboardView.vue # Dashboard view
│   └── package.json          # Frontend dependencies
│
├── uploads/                  # Temporary upload directory
├── README.md                 # Project documentation
└── .env                      # Environment variables
```

## Features

- **Multilingual Support**: The application supports multiple languages, allowing users to translate text between various languages.
- **AI Integration**: Utilizes AI services for enhanced translation capabilities.
- **User-Friendly Interface**: The frontend is built with Vue.js, providing a responsive and interactive user experience.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd agriai
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```

4. Run the backend server:
   ```
   python server.py
   ```

5. Run the frontend application:
   ```
   npm run serve
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.