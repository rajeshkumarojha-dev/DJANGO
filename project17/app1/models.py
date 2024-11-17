from django.db import models

# Create your models here.
class School(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,blank=False)
    uname=models.CharField(max_length=20,blank=False)
    pwd=models.CharField(max_length=20,blank=False)
