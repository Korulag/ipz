from django.contrib import admin

from company_health.apps.feedbacks.models import *

admin.site.register(CompanySatisfaction)
admin.site.register(Feedback)
admin.site.register(PersonalSatisfaction)
admin.site.register(TeamSatisfaction)
