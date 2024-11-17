from django.shortcuts import render
from django.http import HttpResponse
from app1.models import School
# Create your views here.

def register(request):
    id=request.GET['id']
    name=request.GET['name']
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    u=School(id=id,name=name,uname=uname,pwd=pwd)
    u.save()
    response= HttpResponse('Resistered save successfully..')
    return response

def sign(request):
    response=render(request,'app1/index.html')
    return response
