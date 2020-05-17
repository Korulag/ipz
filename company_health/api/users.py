from rest_framework.viewsets import ModelViewSet

from company_health.apps.users.models import User
from company_health.apps.users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    http_method_names = ['delete', 'get', 'post', 'put']
    queryset = User.objects.all()
    serializer_class = UserSerializer
