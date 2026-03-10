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
    delta_state = data.get('deltaState')
    provider = data.get('provider', 'Unknown')
    provider_label = f"{provider} — {delta_state}" if delta_state else provider

    msg = Message(
        subject=f"Insurance Verification - {provider_label}",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']]
    )
    msg.body = (
        f"=== POLICYHOLDER ===\n"
        f"Full Name:      {data.get('fullName')}\n"
        f"Date of Birth:  {data.get('dob')}\n"
        f"Address:        {data.get('address')}\n"
        f"Email:          {data.get('email')}\n"
        f"Phone:          {data.get('phone')}\n\n"
        f"=== INSURANCE ===\n"
        f"Provider:       {provider_label}\n"
        f"ID / SS:        {data.get('insuranceId')}\n"
        f"Employer:       {data.get('employer')}\n"
        f"Employer Phone: {data.get('employerPhone', 'N/A')}\n"
    )

    for file in files:
        msg.attach(file.filename, file.content_type, file.read())

    mail.send(msg)