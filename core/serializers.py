from django.db.models import Count
from rest_framework import serializers

from core import models


class Subject(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'


class Pupil(serializers.ModelSerializer):
    class Meta:
        model = models.Pupil
        fields = '__all__'
