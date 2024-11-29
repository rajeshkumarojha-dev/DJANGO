from django import forms

class Registerform(forms.Form):
    name=forms.CharField(label='name',max_length=20)
    uname=forms.CharField(label='Uname',max_length=20)
    pwd=forms.CharField(label='Password', widget=forms.PasswordInput)