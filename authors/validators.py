from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, name=None):
        self.name = name

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError("Your name must contain letters only!")


@deconstructible
class PasswordValidator:
    def __init__(self, password=None):
        self.password = password

    def __call__(self, value):
        if len(value) != 6 or not value.isdigit():
            raise ValidationError("Your passcode must be exactly 6 digits!")