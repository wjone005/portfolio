# Initialize and bring in different packages

# Import Flask class and reder_template
# url_for function that finds the exact location of routes
from flask import Flask
from flask_mail import Mail 
import os



# Create variable application set to instance of Flask class
# __name__ is the name of the module
# Flask will know where to look for static and template files
application = Flask(__name__)

SECRET_KEY = os.urandom(32)

# Protects website forms from modifiying cookies 
# Open python, import secrets
# Type secrets.token_hex(16)
# Take output and place it below
application.config['SECRET_KEY'] = SECRET_KEY
application.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = 'apikey'
application.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
application.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(application)


# Place here to prevent circular import error
from flask_portfolio import routes
