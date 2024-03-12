from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=56)
    age=models.CharField(max_length=5)
    mobile=models.CharField(max_length=12)
    address=models.CharField(max_length=200)