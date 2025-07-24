from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class ContactForm(FlaskForm):
    name = StringField(
        _('Name'),
        validators=[
            DataRequired(message=_('Please enter your name')),
            Length(min=2, max=100, message=_('Name must be between 2 and 100 characters'))
        ],
        render_kw={"placeholder": _("Your name")}
    )
    
    email = StringField(
        _('Email'),
        validators=[
            DataRequired(message=_('Please enter your email')),
            Email(message=_('Please enter a valid email address'))
        ],
        render_kw={"placeholder": _("your.email@example.com")}
    )
    
    phone = StringField(
        _('Phone'),
        validators=[
            Optional(),
            Length(max=20, message=_('Phone number is too long'))
        ],
        render_kw={"placeholder": _("+34 600 000 000")}
    )
    
    subject = StringField(
        _('Subject'),
        validators=[
            DataRequired(message=_('Please enter a subject')),
            Length(max=200, message=_('Subject is too long'))
        ],
        render_kw={"placeholder": _("How can we help you?")}
    )
    
    message = TextAreaField(
        _('Message'),
        validators=[
            DataRequired(message=_('Please enter your message')),
            Length(min=10, max=2000, message=_('Message must be between 10 and 2000 characters'))
        ],
        render_kw={"rows": 5, "placeholder": _("Your message here...")}
    )
    
    privacy_policy = BooleanField(
        _('I accept the privacy policy'),
        validators=[DataRequired(message=_('You must accept the privacy policy'))]
    )
    
    submit = SubmitField(_('Send Message'))
