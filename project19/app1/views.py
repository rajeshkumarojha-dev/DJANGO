from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
# Create your views here.

def register(request):
    fname=request.GET['fname']
    lname=request.GET['lname']
    phone=request.GET['phone']
    email=request.GET['email']
    password=request.GET['password']

    u=Users(fname=fname,lname=lname,phone=phone,email=email,password=password)
    u.save()
    response = HttpResponse("User Registered successfully......")
    return response


def home(request):
    qs=Users.objects.all()
    response=render(request,'app1/index.html',context={"qs":qs})
    return response

# def display(request):
#     response
