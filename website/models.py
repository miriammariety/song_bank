from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(blank=False, max_length=50)
    lyrics = models.TextField()
    theme = models.ForeignKey(Theme, related_name='songs')


class Theme(models.Model):
    name = models.CharField(blank=False, max_length=50)
