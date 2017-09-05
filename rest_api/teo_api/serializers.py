from rest_framework import serializers
from django.db import models
from .models import Dane


class AuthorSerializer(serializers.ModelSerializer):

    text = models.CharField(max_length=999999, blank=True, null=True)
    author = models.CharField(max_length=999999, blank=True, null=True)

    class Meta:
        model = Dane
        fields = ['text', 'author']
