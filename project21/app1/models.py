from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=30)
    uname=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)

class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    class Meta:
        db_table='Student'