from rest_framework.routers import SimpleRouter

from company_health.api.feedbacks import *
from company_health.api.questionaries import *
from company_health.api.reports import *
from company_health.api.users import UsersViewSet


router = SimpleRouter()

urlpatterns = router.urls + [
    router.register('feedbacks', FeedbackViewSet, basename='feedbacks'),
    router.register('questions', BooleanQuestionViewSet, basename='bool-questions'),
    router.register('questions', RangeQuestionViewSet, basename='range-questions'),
    router.register('reports', CompanyReportViewSet, basename='company-report'),
    router.register('reports', PersonalReportViewSet, basename='personal-report'),
    router.register('reports', TeamReportViewSet, basename='team-report'),
    router.register('satisfactions', CompanySatisfactionViewSet, basename='company-satisfaction'),
    router.register('satisfactions', PersonalSatisfactionViewSet, basename='personal-satisfaction'),
    router.register('satisfactions', TeamSatisfactionViewSet, basename='team-satisfaction'),
    router.register('users', UsersViewSet, basename='users')
]
