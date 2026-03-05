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