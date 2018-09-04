from django.db import models

# Create your models here.

class Ram(models.Model):
    capacity = models.IntegerField()
    vendor = models.CharField(max_length=20)


class Notebook(models.Model):
    model = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    # capacity = models.One