from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.validators import RegexValidator

def validate_artist_email(value):
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError('Invalid email format')

phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits',
    code='invalid_phone'
)
