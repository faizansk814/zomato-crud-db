from django.db import models

# Create your models here.

class Menu(models.Model):
    _id=models.PositiveIntegerField()
    dishname=models.CharField()
    price=models.PositiveIntegerField()
    available=models.CharField()

