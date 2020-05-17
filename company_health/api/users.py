from company_health.api.base import BaseViewSet
from company_health.apps.users.models import User
from company_health.apps.users.serializers import UserSerializer


class UsersViewSet(BaseViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        db_table = 'users'
        managed = True
