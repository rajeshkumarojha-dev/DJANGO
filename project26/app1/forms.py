from django import forms

class UserForm(forms.Form):
    name=forms.CharField(max_length=29)
    uname=forms.CharField(max_length=30)
    pwd=forms.CharField(max_length=20,widget=forms.PasswordInput)