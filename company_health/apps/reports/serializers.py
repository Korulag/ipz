from rest_framework.serializers import ModelSerializer

from company_health.apps.reports.models import *

__all__ = ['CompanyReportSerializer', 'PersonalReportSerializer', 'TeamReportSerializer']


class CompanyReportSerializer(ModelSerializer):

    class Meta:
        model = CompanyReport
        fields = '__all__'


class PersonalReportSerializer(ModelSerializer):

    class Meta:
        model = PersonalReport
        fields = '__all__'


class TeamReportSerializer(ModelSerializer):

    class Meta:
        model = TeamReport
        fields = '__all__'
