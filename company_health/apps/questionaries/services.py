from typing import Union

from parameters_validation import validate_parameters, non_null, non_blank

from company_health.apps.base import BaseService
from company_health.apps.questionaries.models import BooleanMarkQuestion, RangeMarkQuestion

__all__ = ['BooleanMarkQuestionService', 'RangeMarkQuestionService', 'QuestionaryService']


class BaseQuestionService(BaseService):
    model = None

    @classmethod
    @validate_parameters
    def create(cls, category: non_null(non_blank(str)), question: non_null(non_blank(str))):
        return cls.model.objects.create(question_string=question, category=category)


class BooleanMarkQuestionService(BaseQuestionService):
    model = BooleanMarkQuestion


class RangeMarkQuestionService(BaseQuestionService):
    model = RangeMarkQuestion


class QuestionaryService:

    @validate_parameters
    def create_question(self, category: non_null(non_blank(str)), question: non_null(non_blank(str)),
                        q_type: non_null(non_blank(str)) = 'range') -> Union[BooleanMarkQuestion, RangeMarkQuestion]:
        if q_type == 'range':
            return RangeMarkQuestionService.create(category, question)
        return BooleanMarkQuestionService.create(category, question)
