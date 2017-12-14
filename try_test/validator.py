from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid url for this field")
    return value

def validate_dot_com(value):

    if not "com" in value:
        raise forms.ValidationError( "  not .com")

    return value