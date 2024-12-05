from django.shortcuts import render
from app1.forms import UserForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    response=render(request,'app1/index.html')
    return response

def get_temp(request):
    form=UserForm()
    response=render(request,'app1/get.html',context={"form":form})
    return response

def getview(request):
    msg='THIS IS GET METHOD'
    response=HttpResponse(msg)
    return response

def post_temp(request):
    form=UserForm()
    response=render(request,'app1/post.html',context={"form":form})
    return response

def postview(request):
    msg='THIS IS POST METHOD'
    response=HttpResponse(msg)
    return response