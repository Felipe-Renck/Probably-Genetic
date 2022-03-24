from django.contrib.postgres.fields import ArrayField
from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

class Disease(models.Model):
    orpha_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    symptoms = ArrayField(models.CharField(max_length=2000), blank=True, default=list)
    frequencies = ArrayField(models.CharField(max_length=2000), blank=True, default=list)