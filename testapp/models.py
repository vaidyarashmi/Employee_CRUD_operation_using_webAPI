from django.db import models
from django.db.models.fields import CharField

# Create your models here
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100,blank=False)
    esal=models.FloatField()
    eaddr=CharField(max_length=100)