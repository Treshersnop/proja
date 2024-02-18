from rest_framework import viewsets

from core import filters, models, serializers


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.order_by('name')
    serializer_class = serializers.Subject
    filterset_class = filters.Subject


class PupilViewSet(viewsets.ModelViewSet):
    queryset = models.Pupil.objects.all()
    serializer_class = serializers.Pupil
    filterset_class = filters.Pupil
