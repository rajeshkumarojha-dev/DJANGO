from django.db import models

# Create your models here.
class Contacts(models.Model):
    phone=models.CharField(max_length=20,unique=True)
    address=models.CharField(max_length=40)

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact = models.OneToOneField(Contacts, on_delete=models.CASCADE)