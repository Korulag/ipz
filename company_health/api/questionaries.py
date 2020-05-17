from rest_framework.viewsets import ModelViewSet

from company_health.apps.questionaries.models import BooleanMarkQuestion, RangeMarkQuestion
from company_health.apps.questionaries.serializers import (
    BooleanMarkQuestionSerializer,
    RangeMarkQuestionSerializer,
)

__all__ = ['BooleanQuestionViewSet', 'RangeQuestionViewSet']


class BooleanQuestionViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = BooleanMarkQuestion.objects.all()
    serializer_class = BooleanMarkQuestionSerializer


class RangeQuestionViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = RangeMarkQuestion.objects.all()
    serializer_class = RangeMarkQuestionSerializer
