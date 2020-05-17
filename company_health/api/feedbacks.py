from rest_framework.viewsets import ModelViewSet

from company_health.apps.feedbacks.models import *
from company_health.apps.feedbacks.serializers import *

__all__ = ['CompanySatisfactionViewSet', 'FeedbackViewSet', 'PersonalSatisfactionViewSet',
           'TeamSatisfactionViewSet']


class CompanySatisfactionViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = CompanySatisfaction.objects.all()
    serializer_class = CompanySatisfactionSerializer


class FeedbackViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class PersonalSatisfactionViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = PersonalSatisfaction.objects.all()
    serializer_class = PersonalSatisfactionSerializer


class TeamSatisfactionViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = TeamSatisfaction.objects.all()
    serializer_class = TeamSatisfactionSerializer
