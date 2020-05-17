from django.db.models import CharField, DateField, Model, FloatField, EmailField
from django.core.validators import MinValueValidator

__all__ = ['User']


class User(Model):
    name = CharField(max_length=100)
    surname = CharField(max_length=300)
    email = EmailField(max_length=100)
    position = CharField(max_length=100)
    hire_date = DateField()
    level = CharField(max_length=50)
    pay = FloatField(validators=[MinValueValidator(1.)])
