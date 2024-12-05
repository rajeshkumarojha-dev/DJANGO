from django import forms

class Registerform(forms.Form):
    name=forms.CharField(label='name',max_length=20)
    uname=forms.CharField(label='Uname',max_length=20)
    pwd=forms.CharField(label='Password', widget=forms.PasswordInput)
    course=(('1','pyhton'),
            ('2','java'),
            ('3','django'))
    course=forms.ChoiceField(choices=course)
    date=forms.DecimalField(decimal_places=2)