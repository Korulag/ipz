from company_health.api.base import BaseViewSet
from company_health.apps.questionaries.models import BooleanMarkQuestion, RangeMarkQuestion
from company_health.apps.questionaries.serializers import (
    BooleanMarkQuestionSerializer,
    RangeMarkQuestionSerializer,
)

__all__ = ['BooleanQuestionViewSet', 'RangeQuestionViewSet']


class BooleanQuestionViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = BooleanMarkQuestion.objects.all()
    serializer_class = BooleanMarkQuestionSerializer


class RangeQuestionViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = RangeMarkQuestion.objects.all()
    serializer_class = RangeMarkQuestionSerializer
