from django.db import models

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=56)
    age=models.CharField(max_length=5)
    disease=models.CharField(max_length=200)
    status=models.CharField(max_length=30)