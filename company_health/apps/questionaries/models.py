from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)


class Category(ChoiceEnum):
    company = 'Company satisfaction'
    personal = 'Personal satisfaction'
    team = 'Team satisfaction'


class Question(models.Model):
    class Meta:
        abstract = True

    question_string = models.CharField(max_length=1000, null=False)
    category = models.CharField(max_length=10, choices=Category.choices(),
                                default=Category.personal.name)


class RangeMarkQuestion(Question):
    mark = models.PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ], null=True)


class BooleanMarkQuestion(Question):
    mark = models.NullBooleanField(null=True)
