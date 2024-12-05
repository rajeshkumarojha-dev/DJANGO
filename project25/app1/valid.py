from django.core.exceptions import ValidationError
def name_validator(value):
    if not value.isupper():
        raise ValidationError('Name must be in upperCase')
    
def uname_validator(val):
    if not val.isalnum():
        raise ValidationError('uname must be alpha Numeric')

def pwd_validator(val):
    ac,sc,dc=0,0,0
    for ch in val:
        if ch.isalpha():
            ac+=1