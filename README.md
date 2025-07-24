# Paraidesa - Professional Landscaping Website

A modern, responsive, and bilingual (English/Spanish) website for Paraidesa, a professional landscaping business. Built with Flask and Bootstrap 5.

[![Live Demo](https://img.shields.io/badge/View-Live%20Demo-brightgreen)](https://paraidesa.com)  <!-- Update with your actual domain -->

## Features

- 🌍 **Bilingual Support**: Full English and Spanish language support with Flask-Babel
- 📱 **Fully Responsive**: Mobile-first design that works on all devices
- ✉️ **Contact Form**: Secure form with email notifications and validation
- 🖼️ **Portfolio Gallery**: Filterable showcase of landscaping projects
- 🎨 **Modern UI**: Clean, professional design with nature-inspired colors
- 🔒 **Secure**: CSRF protection, form validation, and secure headers
- 📧 **Email Notifications**: Automatic confirmation emails for contact form submissions

## Tech Stack

- **Backend**: Python 3.8+, Flask 2.3.3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Email**: Flask-Mail with async support
- **i18n**: Flask-Babel for translations
- **Forms**: Flask-WTF with CSRF protection
- **Authentication**: Flask-Login for admin access

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajavfer/paraidesa.git
   cd paraidesa
   ```

2. **Set up a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here  # Generate with: python -c 'import secrets; print(secrets.token_hex(16))'
   
   # Email Configuration (for contact form)
   MAIL_SERVER=smtp.your-email-provider.com
   MAIL_PORT=587
   MAIL_USE_TLS=1
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-email-password
   MAIL_DEFAULT_SENDER='Paraidesa <noreply@paraidesa.com>'
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the development server**
   ```bash
   flask run
   ```

7. **Access the application**
   Open your browser and go to: http://localhost:5000

## Project Structure

```
paraidesa/
├── app/
│   ├── __init__.py       # Application factory
│   ├── config.py         # Configuration settings
│   ├── email.py          # Email handling
│   ├── models.py         # Database models
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py     # Application routes
│   │   └── forms.py      # WTForms definitions
│   ├── static/           # Static files (CSS, JS, images)
│   └── templates/        # HTML templates with i18n support
├── migrations/           # Database migrations
├── .flaskenv            # Flask environment variables
├── .env                 # Environment variables (not versioned)
├── requirements.txt     # Python dependencies
└── run.py               # Application entry point
```

## Deployment

### Production Deployment

1. **Set up a production server** (e.g., Gunicorn with Nginx)
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

2. **Set environment to production**
   ```env
   FLASK_ENV=production
   SECRET_KEY=your-production-secret-key
   DATABASE_URL=postgresql://user:password@localhost/paraidesa
   ```

### Platform as a Service (PaaS)

#### Heroku
```bash
# Create a new Heroku app
heroku create paraidesa

# Set environment variables
heroku config:set FLASK_APP=run.py
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key

# Deploy
git push heroku main
```

## Adding New Content

### Adding Portfolio Items
1. Add images to `app/static/images/portfolio/`
2. Update the portfolio items in `app/main/routes.py`

### Adding Translations
1. Extract new strings:
   ```bash
   flask translate update
   ```
2. Edit the `.po` files in `app/translations/`
3. Compile translations:
   ```bash
   flask translate compile
   ```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Website: [paraidesa.com](https://paraidesa.com)
- Email: paraidesa@paraidesa.com
- Phone: +34 670 65 01 70

---

<div align="center">
  Made with ❤️ by Paraidesa Team
</div>
