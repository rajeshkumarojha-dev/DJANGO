from django.shortcuts import render
from app1.models import Employee
# Create your views here.

# def Emp(request):
#     qs=Employee.objects.all()
#     response=render(request,'app1/index.html',context={"qs":qs})
#     return response

def __str__(self):
    print(f'{self.empno},{self.ename},{self.job},{self.sal}')

def filter_data(request):
    job=request.GET['job'] 
    if job != 'all':   
        qs=Employee.objects.filter(job=job)
    else:   
       qs=Employee.objects.all()

    response=render(request,'app1/show.html',context={"qs":qs})
    return response

def home(request):
    response=render(request,'app1/index.html')
    return response
