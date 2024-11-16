from django.db import models

# Create your models here.
class institute(models.Model):
    empno=models.IntegerField()
    ename = models.CharField(max_length=20)
    sal = models.FloatField()