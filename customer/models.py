from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=56)
    mobile=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    purchased_items=models.CharField(max_length=500)
    payable_amount=models.CharField(max_length=50)