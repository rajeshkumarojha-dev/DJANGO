from django.db import models

# Create your models here.
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    sal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'emp'
    
class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'