from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CharField,
    DateField,
    Model,
    PositiveIntegerField,
)

__all__ = ['PersonalReport', 'TeamReport', 'CompanyReport']


class PersonalReport(Model):
    toxicity = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    performance = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    responsiveness = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    responsibility = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    goals_achieved = ArrayField(base_field=CharField(max_length=1000))
    tech_learned = ArrayField(base_field=CharField(max_length=100))
    tools_learned = ArrayField(base_field=CharField(max_length=100))
    salary_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    perks_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    date_created = DateField()


class TeamReport(Model):
    releases_done_on_schedule = PositiveIntegerField()
    releases_missed_schedule = PositiveIntegerField()
    tasks_moved_between_sprints = PositiveIntegerField()
    tasks_had_several_sprints = PositiveIntegerField()
    projects_completed = PositiveIntegerField()
    people_level_upgraded = PositiveIntegerField()
    date_created = DateField()


class CompanyReport(Model):
    salary_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    workplace_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    perks_satisfaction = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    date_created = DateField()
