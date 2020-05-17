__all__ = ['BaseService']


class BaseService:
    model = None

    @classmethod
    def get(cls, id: int):
        return cls.model.objects.get(pk=id)

    @classmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError('Must be realized in child classes')

    @classmethod
    def update(cls, *args, **kwargs):
        return cls.model.objects.update(*args, **kwargs)

    @classmethod
    def delete(cls, *args, **kwargs):
        raise NotImplementedError('Must be realized in child classes')
