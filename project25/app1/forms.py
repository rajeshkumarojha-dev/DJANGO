from django import forms
from django.core import validators
from app1.valid import *
class UserForm(forms.Form):
    name=forms.CharField(max_length=30,validators=[name_validator])
    uname=forms.CharField(max_length=30,validators=[uname_validator])
    email=forms.CharField(validators=[validators.EmailValidator])
    pwd=forms.CharField(max_length=30,validators=[pwd_validator])
    rpwd=forms.CharField(max_length=30,validators=[pwd_validator])

