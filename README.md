# Paraidesa - Professional Landscaping Website

A modern, responsive, and bilingual (English/Spanish) website for Paraidesa, a professional landscaping business. Built with Flask and Bootstrap 5.

![Paraidesa Logo](app/static/images/logo.png)  <!-- Add your logo path here -->

## Features

- 🌍 **Bilingual Support**: Full English and Spanish language support
- 📱 **Fully Responsive**: Looks great on all devices
- ✉️ **Contact Form**: Easy way for clients to get in touch
- 🖼️ **Portfolio Gallery**: Showcase your best work
- 🎨 **Modern UI**: Clean, professional design with nature-inspired colors
- 🚀 **SEO Optimized**: Ready for search engines

## Tech Stack

- **Backend**: Python 3.8+, Flask 2.3.3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Email**: Flask-Mail with async support
- **i18n**: Flask-Babel for translations

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/paraidesa.git
   cd paraidesa
   ```

2. **Create and activate a virtual environment**
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
   Create a `.env` file in the root directory with the following content:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   MAIL_SERVER=smtp.your-email-provider.com
   MAIL_PORT=587
   MAIL_USE_TLS=1
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-email-password
   MAIL_DEFAULT_SENDER='Paraidesa <noreply@paraidesa.com>'
   ```

## Running the Application

1. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

2. **Run the development server**
   ```bash
   flask run
   ```

3. **Access the application**
   Open your browser and go to: http://localhost:5000

## Project Structure

```
paraidesa/
├── app/
│   ├── __init__.py       # Application factory
│   ├── config.py         # Configuration settings
│   ├── email.py          # Email handling
│   ├── models.py         # Database models
│   ├── translations/     # Translation files
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py     # Application routes
│   │   └── forms.py      # WTForms definitions
│   ├── static/           # Static files (CSS, JS, images)
│   └── templates/        # HTML templates
├── migrations/           # Database migrations
├── tests/                # Test files
├── .env.example         # Example environment variables
├── .gitignore
├── config.py            # Main configuration
├── requirements.txt     # Project dependencies
└── run.py               # Application entry point
```

## Adding New Content

### Adding a New Page
1. Create a new template in `app/templates/`
2. Add a new route in `app/main/routes.py`
3. Add the page to the navigation in `app/templates/base.html`

### Adding Translations
1. Extract translatable strings:
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```
2. Initialize a new language (e.g., French):
   ```bash
   pybabel init -i messages.pot -d app/translations -l fr
   ```
3. Update existing translations:
   ```bash
   pybabel update -i messages.pot -d app/translations
   ```
4. Compile translations:
   ```bash
   pybabel compile -d app/translations
   ```

## Deployment

### Heroku
1. Install the Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create`
4. Set environment variables: `heroku config:set KEY=value`
5. Deploy: `git push heroku main`

### PythonAnywhere
1. Upload your code to a Git repository
2. Create a new web app in PythonAnywhere
3. Configure the WSGI file to point to your application
4. Set up environment variables in the web app configuration
5. Reload the web app

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For inquiries, please contact [your-email@example.com](mailto:your-email@example.com)
