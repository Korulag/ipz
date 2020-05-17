from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    FloatField,
    Model,
    NullBooleanField,
    OneToOneField,
    PositiveIntegerField,
)
from django.db.models.deletion import CASCADE

from company_health.apps.users.models import User

__all__ = ['CompanySatisfaction', 'Feedback', 'PersonalSatisfaction', 'TeamSatisfaction']


class PersonalSatisfaction(Model):
    planned = ArrayField(base_field=CharField(max_length=1000))
    done = ArrayField(base_field=CharField(max_length=1000))
    not_done = ArrayField(base_field=CharField(max_length=1000))
    future_plans = ArrayField(base_field=CharField(max_length=1000))
    wanted_position = CharField(max_length=100)
    work_life_balance = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    conference_wanted = NullBooleanField()
    helping_newcomers = NullBooleanField()
    date_created = DateField()


class TeamSatisfaction(Model):
    conflicts = BooleanField()
    team_support = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    team_lead_support = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    tasks_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    project_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    helping_newcomers = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ], null=True)
    date_created = DateField()


class CompanySatisfaction(Model):
    salary_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    workplace_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    perks_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    perks_wanted = ArrayField(base_field=CharField(max_length=100))
    help_others_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ], null=True)
    date_created = DateField()


class Feedback(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    time_in_company = FloatField()
    personal_satisfaction = OneToOneField(PersonalSatisfaction, on_delete=CASCADE)
    team_satisfaction = OneToOneField(TeamSatisfaction, on_delete=CASCADE)
    company_satisfaction = OneToOneField(CompanySatisfaction, on_delete=CASCADE)
    date_created = DateField()
