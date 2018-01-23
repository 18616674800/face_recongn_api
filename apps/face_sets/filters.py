import django_filters
from .models import FaceSets


class FaceSetsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """

    class Meta:
        model = FaceSets
        fields = ['active']

