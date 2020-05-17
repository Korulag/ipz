from parameters_validation import validate_parameters, non_negative, non_null

from company_health.apps.base import BaseService
from company_health.apps.feedbacks.models import Feedback
from company_health.apps.reports.models import *


class PersonalReportService(BaseService):
    model = PersonalReport

    @classmethod
    @validate_parameters
    def create(cls, employee_id: non_negative(non_null(int))) -> model:
        feedback = (Feedback.objects
                    .select_related('user', 'personal_satisfaction', 'team_satisfaction',
                                    'company_satisfaction')
                    .order_by('-id')
                    .filter(user_id=employee_id)
                    .first())
        # TODO: add report generation logic
        return


class TeamReportService(BaseService):
    model = TeamReport

    @classmethod
    @validate_parameters
    def create(cls, team_id: non_negative(non_null(int))) -> model:
        feedbacks = (Feedback.objects
                     .select_related('user', 'personal_satisfaction', 'team_satisfaction',
                                     'company_satisfaction')
                     .order_by('-id')
                     .filter())
        # TODO: add report generation logic
        return


class CompanyReportService(BaseService):
    model = CompanyReport

    @classmethod
    @validate_parameters
    def create(cls, employee_id: non_negative(non_null(int))) -> model:
        feedback = (Feedback.objects
                    .select_related('user', 'personal_satisfaction', 'team_satisfaction',
                                    'company_satisfaction')
                    .order_by('-id')
                    .filter())
        # TODO: add report generation logic
        return
