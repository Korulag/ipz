from company_health.api.base import BaseViewSet
from company_health.apps.feedbacks.models import *
from company_health.apps.feedbacks.serializers import *

__all__ = ['CompanySatisfactionViewSet', 'FeedbackViewSet', 'PersonalSatisfactionViewSet',
           'TeamSatisfactionViewSet']


class CompanySatisfactionViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post']
    queryset = CompanySatisfaction.objects.all()
    serializer_class = CompanySatisfactionSerializer


class FeedbackViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post']
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class PersonalSatisfactionViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post']
    queryset = PersonalSatisfaction.objects.all()
    serializer_class = PersonalSatisfactionSerializer


class TeamSatisfactionViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post']
    queryset = TeamSatisfaction.objects.all()
    serializer_class = TeamSatisfactionSerializer
