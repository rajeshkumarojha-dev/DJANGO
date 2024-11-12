from django.shortcuts import render

# Create your views here.

def calculator(request):
    num1 = eval(request.GET['num1'])
    num2 = eval(request.GET['num2'])
    num3=num1+num2
    response = render(request,'app1/add.html',context={"num3":num3,"num1":num1,"num2":num2})
    return response

def home(request):
    response = render(request,'app1/home.html')
    return response


def product(request):
    product_data={'apple':[1200,'apple.avif'],
                  'ball':[1150,'ball.avif'],
                  'cat':[1800,'cat.jpg'],
                  'dog':[1350,'dog.avif'],
                  'lion':[2490,'lion.avif']
                  }
    response = render(request,'app1/product.html',context={"product_data":product_data})
    return response

def filter(request):
    names=['rajesh','puja','riya','sradha']
    emp_data=[{'empNo':101,"name":"Rajesh","sal":12000},
              {'empNo':102,"name":"Puja","sal":20000},
              {'empNo':103,"name":"sardha","sal":12500},
              {'empNo':104,"name":"krishna","sal":11000},
              {'empNo':105,"name":"biswa","sal":21000}]
    course=['python','sql','mongodb','django',['HTML','CSS','JS']]
    
    response = render(request,'app1/filter.html',context={"names":names,"emp_data":emp_data,"course":course})
    return response


    