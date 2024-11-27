from django.db import models

# Create your models here.

class Dept(models.Model):
    deptNo=models.IntegerField(primary_key=True)
    deptName=models.CharField(max_length=30)

class Employee(models.Model):    
    empName=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    salery=models.FloatField()
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)