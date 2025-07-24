from flask import current_app, render_template
from flask_mail import Message
from app import mail
from threading import Thread
from flask_babel import _

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            current_app.logger.error(f"Error sending email: {str(e)}")

def send_email(subject, sender, recipients, text_body, html_body, reply_to=None):
    msg = Message(
        subject=subject,
        sender=sender,
        recipients=recipients,
        reply_to=reply_to
    )
    msg.body = text_body
    msg.html = html_body
    
    # Send email asynchronously
    Thread(
        target=send_async_email,
        args=(current_app._get_current_object(), msg)
    ).start()

def send_contact_email(contact_data):
    """
    Send a contact form submission email.
    
    Args:
        contact_data (dict): Dictionary containing:
            - name: Sender's name
            - email: Sender's email
            - phone: Sender's phone number (optional)
            - subject: Email subject
            - message: Email message
            - language: Language code for i18n
    """
    # Admin email (configured in config.py)
    admin_email = current_app.config['MAIL_USERNAME']
    
    # Set language for email templates
    lang = contact_data.get('language', 'en')
    
    # Email subject
    subject = f"New Contact Form: {contact_data['subject']}"
    
    # Render email templates
    text_body = render_template(
        f'email/contact_{lang}.txt',
        **contact_data
    )
    
    html_body = render_template(
        f'email/contact_{lang}.html',
        **contact_data
    )
    
    # Send email
    send_email(
        subject=subject,
        sender=current_app.config['MAIL_DEFAULT_SENDER'],
        recipients=[admin_email],
        text_body=text_body,
        html_body=html_body,
        reply_to=f"{contact_data['name']} <{contact_data['email']}>"
    )
    
    # Send confirmation email to the user
    send_confirmation_email(contact_data)

def send_confirmation_email(contact_data):
    """Send a confirmation email to the person who filled the contact form."""
    lang = contact_data.get('language', 'en')
    
    subject = _('Thank you for contacting us')
    
    text_body = render_template(
        f'email/confirmation_{lang}.txt',
        **contact_data
    )
    
    html_body = render_template(
        f'email/confirmation_{lang}.html',
        **contact_data
    )
    
    send_email(
        subject=subject,
        sender=current_app.config['MAIL_DEFAULT_SENDER'],
        recipients=[contact_data['email']],
        text_body=text_body,
        html_body=html_body
    )
