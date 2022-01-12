from django_filters import rest_framework as filters
from .models import Answer


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnswerFilter(filters.FilterSet):
    user = CharFilterInFilter(
        field_name='user', lookup_expr='in', label='user ID')

    class Meta:
        model = Answer
        fields = ['user']
