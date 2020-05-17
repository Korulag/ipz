from django.contrib import admin

from company_health.apps.reports.models import *

admin.site.register(CompanyReport)
admin.site.register(PersonalReport)
admin.site.register(TeamReport)
