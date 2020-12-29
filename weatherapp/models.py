from django.db import models


# Create your models here.
class Teste(models.Model):
    cidade = models.CharField(max_length=100)
