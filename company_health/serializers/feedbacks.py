from rest_framework.serializers import ModelSerializer, Serializer

from company_health.models.feedbacks import *

__all__ = ['CompanySatisfactionSerializer', 'FeedbackSerializer', 'PersonalSatisfactionSerializer',
           'TeamSatisfactionSerializer']


class PersonalSatisfactionSerializer(ModelSerializer):
    class Meta:
        model = PersonalSatisfaction
        fields = '__all__'


class TeamSatisfactionSerializer(ModelSerializer):
    class Meta:
        model = TeamSatisfaction
        fields = '__all__'


class CompanySatisfactionSerializer(ModelSerializer):
    class Meta:
        model = CompanySatisfaction
        fields = '__all__'


class FeedbackSerializer(Serializer):
    personal_satisfaction = PersonalSatisfactionSerializer(required=True)
    team_satisfaction = TeamSatisfactionSerializer(required=True)
    company_satisfaction = CompanySatisfactionSerializer(required=True)
