from django.shortcuts import render
from app1.models import *
# Create your views here.
def home(request):
    qs=Dept.objects.all()
    dept=[]
    for row in qs:
        dept.append(row.deptName)
    response=render(request,'app1/index.html',context={'dept':dept})
    return response

def departTemp(request):
    response=render(request,'app1/addDept_temp.html')
    return response

def department(request):
    deptNo=int(request.GET['deptNo'])
    deptname=request.GET['dname']
    try:
        d=Dept.objects.create(deptNo=deptNo,deptName=deptname)
        d.save()
        msg='DEPARTMENT ADDED SUCCESSFULLY..........'
    except:
      msg="ALREADY EXIST"
      
    response=render(request,'app1/addDept_temp.html',context={'msg':msg})
    return response

def emp_temp(request):
    qs=Dept.objects.all()
    dept=[]
    for row in qs:
        dept.append(row.deptName)
    response=render(request,'app1/addEmp.html',context={'dept':dept})
    return response

def addemp(request):
    ename=request.GET['ename']
    job=request.GET['job']
    sal=float(request.GET['sal'])
    deptName=request.GET['deptName']
    try:
        dept=Dept.objects.get(deptName=deptName)
        e=Employee.objects.create(empName=ename,job=job,salery=sal,dept=dept)
        e.save()
        msg="Employee added successfully"
    except:
        msg='Employee exist already'
    response=render(request,'app1/addEmp.html',context={'msg':msg})
    return response

