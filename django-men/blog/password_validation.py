from gettext import ngettext
from django.core.exceptions import ValidationError



#   Dodałem celowe zasady słabych haseł. Silne są nudne

#   Hasła muszą być krótrze niż 10 znaków
#   Nie zawierać znaków specjalnych
#   Sukcesywne cyfry nie mogą się różnić o więcej niż 1
#   Cyfry muszą być w 1 ciągu
class MaximumLengthValidator:
    def __init__(self, max_length=10):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                ngettext(
                    "This password is too long. It cannot contain more than %(max_length)d character.",
                    "This password is too long. It cannot contain more than %(max_length)d characters.",
                    self.max_length
                ),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return ngettext(
            "Your password cannot contain more than %(min_length)d characters.",
            "Your password cannot contain more than %(min_length)d characters.",
            self.min_length
        ) % {'max_length': self.max_length}

class NoSpecialCharactersValidator:
    def validate(self, password, user=None):
        if any(not char.isalnum() for char in password):
            raise ValidationError("Password cannot contain special characters")

    def get_help_text(self):
        return "Your password cannot cannot contain special characters"

    
class NoWeirdNumbersValidator:
    def validate(self, password, user=None):
        numbers_found = False
        for i in range(1, len(password)):
            char = password[i]
            if char.isdigit():
                if not numbers_found:
                    if 0 < i < len(password) - 1:
                        previous_number = password[i - 1]
                        if previous_number.isdigit():
                            previous_number = int(previous_number)
                            number = int(char)
                            difference = abs(previous_number - number)
                            if difference > 1:
                                ValidationError("Subsequent numbers cannot differ by more than one")
                        next_number = password[i + 1]
                        if not next_number.isdigit():
                            numbers_found = True
                else:
                    raise ValidationError("Password cannot contain two sequences of numbers")

    def get_help_text(self):
        return "Your password cannot contain two sequences of numbers and they cannot differ from each other by more than one"