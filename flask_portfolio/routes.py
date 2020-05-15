# Import Flask class and reder_template
# url_for function that finds the exact location of routes
from flask import render_template, url_for, flash, redirect, request, Flask, session

from flask_portfolio.forms import ContactForm

from flask_portfolio import application, mail

from flask_mail import Message




# return "Home Page!" to root or homepage both are the same
@application.route("/", methods=['GET', 'POST'])
@application.route("/layout", methods=['GET', 'POST'])
@application.route("/home", methods=['GET', 'POST'])

def home():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit() == False:
            flash('All fields are required.', 'danger')
            return render_template('home.html', form=form)
        else:
            #flash('Email sent successfully')
            recipient = request.form['email']
            msg = Message(form.subject.data, recipients=[recipient])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            #render_template('home.html', success=True)
            flash('Email sent successfully', 'success')
            return redirect(url_for('home'))  #render_template('home.html', success=True)
    elif request.method == 'GET':
        return render_template('home.html', form=form)        
    
        #else:
            #return 'Form posted'

