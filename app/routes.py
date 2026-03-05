from flask import Blueprint, request, jsonify
from .mailer import send_contact_email
from .validators import validate_contact

bp = Blueprint('api', __name__)

@bp.route('/contact', methods=['POST'])
def contact():
    # Parsear según content-type
    if request.content_type.startswith('multipart/form-data'):
        data = request.form.to_dict()
        files = request.files.getlist('images')
    else:
        data = request.get_json() or {}
        files = []

    errors = validate_contact(data)
    if errors:
        return jsonify({"ok": False, "errors": errors}), 422

    send_contact_email(data, files)
    return jsonify({"ok": True, "message": "Correo enviado"}), 200