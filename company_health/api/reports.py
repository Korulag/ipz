from company_health.api.base import BaseViewSet
from company_health.apps.reports.models import *
from company_health.apps.reports.serializers import *

__all__ = ['CompanyReportViewSet', 'PersonalReportViewSet', 'TeamReportViewSet']


class CompanyReportViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer


class PersonalReportViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = PersonalReport.objects.all()
    serializer_class = PersonalReportSerializer


class TeamReportViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = TeamReport.objects.all()
    serializer_class = TeamReportSerializer
