from django.db import models

# Create your models here.

class Users(models.Model):
    fname=models.CharField(max_length=30,blank=False)
    lname=models.CharField(max_length=30,blank=False)
    phone=models.CharField(max_length=12,blank=False)
    email=models.CharField(max_length=70,blank=False)
    password=models.CharField(max_length=12,blank=False)

