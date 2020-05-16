from datetime import date

from django.test import TestCase
from rest_framework.serializers import ValidationError

from company_health.serializers.users import UserSerializer


class TestUserSerializer(TestCase):

    def test_negative_null_data(self):
        serializer = UserSerializer(data=None)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_negative_empty_data(self):
        serializer = UserSerializer(data={})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_negative_not_enough_data(self):
        serializer = UserSerializer(data={'name': 'John', 'surname': 'Doe'})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_positive(self):
        data = {'name': 'John', 'surname': 'Doe', 'position': 'Team Lead',
                'hire_date': date.today(), 'level': 'Senior'}
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
