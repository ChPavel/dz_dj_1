from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


""" Валидатор для поля age модели User"""

def check_birth_date(birth_date):
    diff = relativedelta(date.today(), birth_date).years
    if diff < 9:
        raise ValidationError("Запрещена регистрация пользователей младше 9 лет.")
