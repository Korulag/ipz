from django.db.models import CharField, DateField, Model

__all__ = ['User']


class User(Model):
    name = CharField(max_length=100)
    surname = CharField(max_length=300)
    position = CharField(max_length=100)
    hire_date = DateField()
    level = CharField(max_length=50)
