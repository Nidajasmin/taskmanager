from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    date=models.DateField()
    time=models.TimeField()
