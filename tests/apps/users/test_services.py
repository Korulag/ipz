from ddt import data, ddt
from django.core.exceptions import ValidationError
from django.test import TestCase

from company_health.apps.users.services import UserService


invalid_test_data = (
    (None, ) * 6,
    ('John', ) + (None, ) * 5,
    ('John', 'Doe', ) + (None, ) * 4,
    ('John', 'Doe', 'Team Lead') + (None, ) * 3,
    ('John', 'Doe', 'Team Lead', 'Senior') + (None, ) * 2,
    ('John', 'Doe', 'Team Lead', 'Senior', 'invalid email', None),
    (1, 'Doe', 'Team Lead', 'Senior', 'invalid email', 2600.),
    ('John', 1, 'Team Lead', 'Senior', 'invalid email', 2600.),
    ('John', 'Doe', 1, 'Senior', 'invalid email', 2600.),
    ('John', 'Doe', 'Team Lead', 1, 'invalid email', 2600.),
    ('John', 'Doe', 'Team Lead', 'Senior', 1, 2600.),
    ('John', 'Doe', 'Team Lead', 'Senior', 'invalid email', 'some salary'),
    ('John', 'Doe', 'Team Lead', 'Senior', 'invalid email', 2600.),
)


@ddt
class TestUserService(TestCase):

    @data(*invalid_test_data)
    def test_negative_create_user_empty_or_invalid_data(self, input_data):
        with self.assertRaises(ValueError, RuntimeError, ValidationError):
            UserService.create(*input_data)

    def test_positive(self):
        data = ('John', 'Doe', 'Team Lead', 'Senior', 'john.doe@supercompany.com', 2600.),
        user = UserService.create(*data)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, data[0])
        self.assertEqual(user.surname, data[1])
        self.assertEqual(user.position, data[2])
        self.assertEqual(user.level, data[3])
        self.assertEqual(user.email, data[4])
        self.assertEqual(user.pay, data[5])
