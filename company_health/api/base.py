from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_value_regex = r'[0-9]*'
