from django.shortcuts import render
from app1.models import Users
from django.db.models import Q
# Create your views here.
def home(request):
    response=render(request,'app1/index.html')
    return response

def sign_temp(request):
    response=render(request,'app1/signup.html')
    return response

def signup(request):
    name=request.GET['name']
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    qs=Users.objects.filter(uname=uname)
    if len(qs) == False:
        u=Users(name=name,uname=uname,password=pwd)
        u.save()
        msg='User Resistered'
    else:
        msg='User Exist'

    response=render(request,'app1/signin.html',context={'msg':msg})
    return response

def signin_temp(request):
    response=render(request,'app1/signin.html')
    return response

def signin(request):
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    try:
        qs=Users.objects.get(uname=uname,password=pwd)
        response=render(request,'app1/welcome.html',context={'qs':qs,'msg':'Login Successfully  '})
        return response
    except:
        response=render(request,'app1/signin.html',context={"msg":'Wrong username and password'})
        return response
    
def change_temp(request):
    response=render(request,'app1/change.html')
    return response

def change(request):
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    npwd=request.GET['npwd']

    try:
        u=Users.objects.get(uname=uname,password=pwd)
        u.password=npwd
        u.save()
        msg='Updated successfully'
    except:
        msg='Invalid username'
    response=render(request,'app1/change.html',context={'msg':msg})
    return response

def delete_temp(request):
    response=render(request,'app1/delete.html')
    return response

def delete(request):
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    try:
        qs=Users.objects.get(uname=uname,password=pwd)
        qs.delete()
        msg="Deleted successfully"
    except:
        msg="Invalids Username"
    response=render(request,'app1/delete.html',context={"msg":msg})
    return response
    