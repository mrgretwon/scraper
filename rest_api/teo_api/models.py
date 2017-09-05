from __future__ import unicode_literals

from django.db import models


# Model wygenerowany automatycznie
# python manage.py inspectdb > models.py

class Dane(models.Model):
    text = models.CharField(max_length=999999, blank=True, null=True)
    author = models.CharField(max_length=999999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dane'
