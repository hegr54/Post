from django.core.exceptions import ValidationError

def validate_author_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("¡No es email valido")

def validate_algo(value):
    if "algo" in value:
        return value
    else:
        raise ValidationError("¡Esta extencion es incorrecta")
