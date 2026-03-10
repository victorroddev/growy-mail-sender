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
        errors.append("Full name is required")
    if not data.get('dob'):
        errors.append("Date of birth is required")
    if not data.get('address'):
        errors.append("Address is required")
    if not data.get('email') or '@' not in data.get('email', ''):
        errors.append("Invalid email")
    if not data.get('phone'):
        errors.append("Phone number is required")
    if not data.get('provider'):
        errors.append("Insurance provider is required")
    if not data.get('insuranceId'):
        errors.append("Insurance ID is required")
    if not data.get('employer'):
        errors.append("Employer is required")
    # Si es Delta Dental, el estado es obligatorio
    if data.get('provider', '').lower().find('delta') != -1 and not data.get('deltaState'):
        errors.append("State is required for Delta Dental plans")
    return errors