from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=20,blank=False)
    uname=models.CharField(max_length=30, primary_key=True)
    password=models.CharField(max_length=12,blank=False)