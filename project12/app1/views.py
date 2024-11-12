from django.shortcuts import render

# Create your views here.

def show_data(request):
    emp_data=[
        {"id":101,"empName":"Rajesh","salery":12000},
        {"id":102,"empName":"Suresh","salery":22000},
        {"id":103,"empName":"zebra","salery":12500},
        {"id":104,"empName":"baaj","salery":20000},
        {"id":105,"empName":"puja","salery":21000},
    ]
    response=render(request,'app1/index.html',context={"emp_data":emp_data})
    return response

def displayData_upper(request):
    names=['rajesh','radha','puja','sradha']
    response = render(request,'app1/upper.html',context={"names":names})
    return response
    
def display_data(request):
    course=['python','java','sql',['HTML','CSS','JS']]
    response = render(request,'app1/list.html',context={'course':course})
    return  response