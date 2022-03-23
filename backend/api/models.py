from django.db import models
from django.contrib.postgres.fields import ArrayField


class Disorder(models.Model):
    orpha_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    symptoms = ArrayField(models.CharField(max_length=2000), blank=True, default=list)
