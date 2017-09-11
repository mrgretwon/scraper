from __future__ import unicode_literals

from django.db import models


# model created by:
# python manage.py inspectdb > models.py

class Data(models.Model):
    text = models.CharField(max_length=20000, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'
