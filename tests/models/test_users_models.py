from datetime import date
from django.test import TestCase

from company_health.models.users import User


class TestUserModel(TestCase):

    def test_negative_save_int_into_str_field(self):
        user = User()
        with self.assertRaises(TypeError):
            user.name = 1
            user.save()

    def test_negative_save_str_into_date_field(self):
        user = User()
        with self.assertRaises(TypeError):
            user.hire_date = "test"
            user.save()

    def test_positive(self):
        params = {'name': 'John', 'surname': 'Doe', 'position': 'Team Lead',
                  'hire_date': date.today(), 'level': 'Senior'}
        user = User(**params)
        user.save()
        test_user = User.objects.get(user.id)
        self.assertDictEqual(test_user.__dict__, params)
