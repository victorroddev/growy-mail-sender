from flask import Blueprint, request, jsonify
from .mailer import send_contact_email, send_insurance_email
from .validators import validate_contact, validate_insurance

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

#route for insurance modal.
@bp.route('/validate-insurance', methods=['POST'])
def validate_insurace():
    data = request.form.to_dict()
    files = [request.files.get('frontID'), request.files.get('backID')]
    files = [f for f in files if f] #filter if any one is none.

    errors= validate_insurance(data)
    if errors:
        return jsonify({"ok": False, "errors": errors}), 422


    send_insurance_email(data, files)
    return jsonify({"ok": True, "message": "Correo enviado"}), 200