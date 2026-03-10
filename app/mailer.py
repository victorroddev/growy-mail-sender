from flask_mail import Message
from flask import current_app
from . import mail

def send_contact_email(data, files=[]):
    msg = Message(
        subject=f"Contacto: {data.get('subject', 'Sin asunto')}",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']]
    )
    msg.body = f"Nombre: {data.get('name')}\nEmail: {data.get('email')}\n\n{data.get('message')}"

    for file in files:
        msg.attach(file.filename, file.content_type, file.read())

    mail.send(msg)

def send_insurance_email(data, files=[]):
    msg = Message(
        subject=f"Insurance Validation - {data.get('provider', 'Unknown')}",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']]
    )
    msg.body = (
        f"Fulll Name: {data.get('fullName')}\n"
        f"Email: {data.get('email')}\n"
        f"Phone: {data.get('phone')}\n"
        f"Provider: {data.get('provider')}\n"
    )

    for file in files:
        msg.attach(file.filename, file.content_type, file.read())

    mail.send(msg)