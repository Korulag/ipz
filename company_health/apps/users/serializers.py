from rest_framework import serializers

from company_health.apps.users.models import User

__all__ = ['UserSerializer']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
