from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if age < 1 or age > 120:
        raise ValidationError(
            'Ожидаемый возраст от 1 года до 120 лет'
        )