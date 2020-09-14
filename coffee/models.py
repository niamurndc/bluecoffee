from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

# class Coffee(models.Model):
#   name = models.CharField(max_length=50)
#   category = models.CharField(max_length=30)
#   special = models.

class Coffe(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=30)
  items = ArrayField(models.CharField(max_length=200), blank=True)

  def __str__(self):
      return self.name
  
  
