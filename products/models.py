from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FLoatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    