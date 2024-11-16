from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
# Create your views here.
def resister(request):
    name=request.GET['name']
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    u=Users(name=name,uname=uname,password=pwd)
    u.save()
    response = HttpResponse("Resister saved")
    return response

def signUp(request):
    response=render(request,'app1/index.html')
    return response