import django_filters
from django.db.models import F, Q, QuerySet

from core import models


class Subject(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Subject
        fields = '__all__'


class UserProfile(django_filters.FilterSet):
    full_name = django_filters.CharFilter(method='filter_full_name')
    birthday = django_filters.DateFilter(method='filter_birthday')

    def filter_full_name(self, qs: QuerySet, name: str, value: any) -> QuerySet[models.UserProfile]:
        for value in value.split():
            qs = qs.filter(
                Q(first_name__icontains=value) |
                Q(last_name__icontains=value) |
                Q(patronymic__icontains=value)
            )
        return qs

    def filter_birthday(self, qs: QuerySet, name: str, value: any) -> QuerySet[models.UserProfile]:
        qs = qs.filter(birth_date__lte=value)
        return qs


class Pupil(UserProfile):
    class Meta:
        model = models.Pupil
        exclude = ('photo',)
