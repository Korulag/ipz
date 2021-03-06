from datetime import date

from django.core.validators import validate_email
from parameters_validation import (
    validate_parameters,
    non_null,
    non_blank,
    non_negative,
)

from company_health.apps.base import BaseService
from company_health.apps.users.models import User


class UserService(BaseService):
    model = User

    @classmethod
    @validate_parameters
    def create(cls, name: non_null(non_blank(str)), surname: non_null(non_blank(str)),
               position: non_null(non_blank(str)), level: non_null(non_blank(str)),
               email: non_null(non_blank(str)), pay: non_negative(non_null(int))) -> User:
        validate_email(email)
        return cls.model.objects.create(name=name, surname=surname, position=position,
                                        hire_date=date.today(), level=level, email=email, pay=pay)
