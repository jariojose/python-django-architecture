from django.db import models


# Create your models here.

class Ram(models.Model):
    capacity = models.IntegerField()
    vendor = models.CharField(max_length=20)


class CPU(models.Model):
    core = models.CharField(max_length=2, default='3')
    MODEL_VENDOR = (
        ('I3', 'Intel Core I3'),
        ('I5', 'Intel Core I5'),
        ('I7', 'Intel Core I7'),
        ('E7', 'AMD EPYC 7551')
    )
    model_vendor = models.CharField(max_length=2, choices=MODEL_VENDOR, default='I3')


class Storage(models.Model):
    CAPACITY = (
        ('HD', 'HD 120GB'),
        ('SSD', 'SSD 120GB')
    )
    capacity = models.CharField(max_length=3, choices=CAPACITY, default='HD')


class Notebook(models.Model):
    model = models.CharField(max_length=20)
    VENDOR = (
        ('HP', 'Hewlett Packard'),
        ('DELL', 'Dell Corporation'),
        ('SAMSUNG', 'Samsung Corporation'),
        ('AVELL', 'High Performance')
    )
    vendor = models.CharField(max_length=8, choices=VENDOR, null=True)
    description = models.CharField(max_length=100)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE, null=True)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
