from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
# Create your views here.
def resister(request):
    names=request.GET['names']
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    u=Users(name=names,uname=uname,passward=pwd)
    u.save()
    response=HttpResponse("User Resistered.....")
    return response

def signUp(request):
    response=render(request,'app1/index.html')
    return response