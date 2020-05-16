__all__ = ['BaseService']


class BaseService:
    model = None

    def create(self, **data):
        raise NotImplementedError('Must be realized in child classes')

    def update(self, **data):
        raise NotImplementedError('Must be realized in child classes')

    def delete(self, **data):
        raise NotImplementedError('Must be realized in child classes')
