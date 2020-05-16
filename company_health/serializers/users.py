from rest_framework import serializers

from company_health.models.users import User

__all__ = ['UserSerializer']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
