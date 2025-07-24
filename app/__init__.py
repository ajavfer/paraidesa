from flask import Flask, request, session, g, current_app
from flask_babel import Babel
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config
from datetime import datetime

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
babel = Babel()
login_manager = LoginManager()
mail = Mail()
login_manager.login_view = 'main.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Add current year to template context
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # Set up language selection
    @app.before_request
    def before_request():
        # Check URL parameter for language first
        lang = request.args.get('lang')
        if lang in app.config['LANGUAGES']:
            session['language'] = lang
        # Fall back to session or default language
        g.current_language = session.get('language', app.config['BABEL_DEFAULT_LOCALE'])
    
    # Import models after app is created to avoid circular imports
    with app.app_context():
        from app import models
        # Create database tables if they don't exist
        db.create_all()
    
    return app
