def validate_contact(data):
    errors = []
    if not data.get('name'):
        errors.append("El nombre es requerido")
    if not data.get('email') or '@' not in data.get('email', ''):
        errors.append("Email inválido")
    if not data.get('message'):
        errors.append("El mensaje es requerido")
    return errors

def validate_insurance(data):
    errors = []
    if not data.get('fullName'):
        errors.append("El nombre es requerido")
    if not data.get('email') or '@' not in data.get('email', ''):
        errors.append("Email inválido")
    if not data.get('phone'):
        errors.append("El teléfono es requerido")
    if not data.get('provider'):
        errors.append("El proveedor de seguro es requerido")
    return errors