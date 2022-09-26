from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.IntegerField()