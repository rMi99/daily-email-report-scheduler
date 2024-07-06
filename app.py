from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import email_scheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class EmailForm(FlaskForm):
    smtp_server = StringField('SMTP Server', validators=[DataRequired()])
    smtp_port = StringField('SMTP Port', validators=[DataRequired()])
    smtp_username = StringField('Email', validators=[DataRequired(), Email()])
    smtp_password = PasswordField('Password', validators=[DataRequired()])
    to_email = StringField('Recipient Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Schedule Email')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm()
    if form.validate_on_submit():
        email_details = {
            'smtp_server': form.smtp_server.data,
            'smtp_port': int(form.smtp_port.data),
            'smtp_username': form.smtp_username.data,
            'smtp_password': form.smtp_password.data,
            'to_email': form.to_email.data,
            'subject': form.subject.data,
            'body': form.body.data
        }
        email_scheduler.schedule_email(email_details)
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
