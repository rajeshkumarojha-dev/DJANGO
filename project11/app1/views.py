from django.shortcuts import render

# Create your views here.
def python(request):
    response = render(request,'app1/python.html')
    return response

# def java(request):
#     response = render(request,'app1/java.html')
#     return response

def home(request):
    response = render(request,'app1/index.html')
    return response

def add_number(request):
    num1=eval(request.GET['num1'])
    num2=eval(request.GET['num2'])
    num3=num1+num2
    response = render(request,'app1/add.html',context={'num1':num1,'num2':num2,'num3':num3})
    return response

def product_data(request):
    product={'Apple':[101,'apple.avif'],
             'Ball':[102,'ball.avif'],
             'Cat':[203,'cat.jpg'],
             'Dog':[302,'dog.avif'],
             'Lion':[402,'lion.avif'],
             'Orange':[362,'orange.avif'],
             'Fish':[102,'fish.avif']}
    response=render(request,'app1/java.html',context={"product":product})
    return response