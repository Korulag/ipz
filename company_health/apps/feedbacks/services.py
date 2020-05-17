from company_health.apps.base import BaseService
from company_health.apps.feedbacks.models import (
    CompanySatisfaction,
    Feedback,
    PersonalSatisfaction,
    TeamSatisfaction,
)


class FeedbackService(BaseService):
    model = Feedback


class CompanySatisfactionService(BaseService):
    model = CompanySatisfaction


class PersonalSatisfactionService(BaseService):
    model = PersonalSatisfaction


class TeamSatisfactionService(BaseService):
    model = TeamSatisfaction
