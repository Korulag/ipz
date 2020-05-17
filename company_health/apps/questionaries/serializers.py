from rest_framework.serializers import ModelSerializer

from company_health.apps.questionaries.models import BooleanMarkQuestion, RangeMarkQuestion


class BooleanMarkQuestionSerializer(ModelSerializer):
    class Meta:
        model = BooleanMarkQuestion
        fields = '__all__'


class RangeMarkQuestionSerializer(ModelSerializer):
    class Meta:
        model = RangeMarkQuestion
        fields = '__all__'
