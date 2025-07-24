from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Project(db.Model):
    """Project model for portfolio items"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))
    
    # For translations
    title_en = db.Column(db.String(100))
    description_en = db.Column(db.Text)
    
    def get_title(self, language='es'):
        return self.title_en if language == 'en' and self.title_en else self.title
    
    def get_description(self, language='es'):
        return self.description_en if language == 'en' and self.description_en else self.description

class User(UserMixin, db.Model):
    """User model for admin access"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
