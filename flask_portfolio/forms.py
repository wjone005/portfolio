from flask_wtf import FlaskForm, RecaptchaField, Form

from wtforms import StringField, TextAreaField, SubmitField, validators

from wtforms.validators import InputRequired, Length, Email, EqualTo


class ContactForm(Form):
    name = StringField("Name", validators=[InputRequired("Please enter your name.")])
    email = StringField("Email", [validators.InputRequired("Please enter your email address."), validators.Email("Enter a valid email address", check_deliverability=True)])
    subject = StringField("Subject", [validators.InputRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.InputRequired("Please enter a message")])
    #recaptcha = RecaptchaField()
    submit = SubmitField("Send")