from flask import render_template, redirect, url_for, request, current_app, g, flash, session
from flask_babel import _, get_locale
from app.main import bp
from app.main.forms import ContactForm
from app.email import send_contact_email
from app import db
import os

@bp.route('/')
@bp.route('/<lang_code>/')
def index():
    return render_template('index.html', title=_('Home'))

@bp.route('/about')
@bp.route('/<lang_code>/about')
def about():
    return render_template('about.html', title=_('About Us'))

@bp.route('/services')
@bp.route('/<lang_code>/services')
def services():
    return render_template('services.html', title=_('Services'))

@bp.route('/portfolio')
@bp.route('/<lang_code>/portfolio')
def portfolio():
    return render_template('portfolio.html', title=_('Portfolio'))

@bp.route('/contact', methods=['GET', 'POST'])
@bp.route('/<lang_code>/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Get the current language
            lang_code = get_locale().language
            
            # Prepare email data
            email_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data or 'Not provided',
                'subject': form.subject.data,
                'message': form.message.data,
                'language': lang_code
            }
            
            # Send email
            send_contact_email(email_data)
            
            # Log the contact (optional)
            # contact = ContactMessage(
            #     name=form.name.data,
            #     email=form.email.data,
            #     phone=form.phone.data,
            #     subject=form.subject.data,
            #     message=form.message.data
            # )
            # db.session.add(contact)
            # db.session.commit()
            
            # Show success message
            flash(_('Thank you for your message. We will get back to you soon!'), 'success')
            return redirect(url_for('main.contact'))
            
        except Exception as e:
            current_app.logger.error(f'Error sending contact form: {str(e)}')
            flash(_('An error occurred while sending your message. Please try again later.'), 'danger')
    
    # Handle GET request or form validation errors
    return render_template('contact.html', title=_('Contact Us'), form=form)

@bp.route('/set_language/<language>')
def set_language(language=None):
    if language in current_app.config['LANGUAGES']:
        # Store the language in the session
        session['language'] = language
    # Redirect back to the previous page or home
    return redirect(request.referrer or url_for('main.index'))
