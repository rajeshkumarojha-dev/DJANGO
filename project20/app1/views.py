from django.shortcuts import render
from app1.models import Marks
# Create your views here.
def home(request):
    student=Marks.objects.all() 
    response=render(request,'app1/index.html',context={'student':student})
    return response

def add_student_temp(request):
    response=render(request,'app1/addstudent.html')
    return response

def add_student(request):
    rno=int(request.GET['rno'])
    name=request.GET['name']
    sub1=float(request.GET['sub1'])
    sub2=float(request.GET['sub2'])
    m=Marks(rollno=rno,name=name,sub1=sub1,sub2=sub2)
    m.save()
    response=render(request,'app1/addstudent.html',context={"msg":"added successfully...."})
    return response

def update_student_temp(request):
    response=render(request,'app1/updatestudent.html')
    return response

def update_student(request):
    rno=int(request.GET['rno'])
    sub1=float(request.GET['sub1'])
    sub2=float(request.GET['sub2'])
    try:
        student=Marks.objects.get(rollno=rno)
        student.sub1=sub1
        student.sub2=sub2
        student.save()
        response=render(request,'app1/updatestudent.html',context={"msg":"updated successfully...."})
    except:
        response=render(request,'app1/updatestudent.html',context={"msg":"Invalids...."})
    return response

def delete_student_temp(request):
    response=render(request,'app1/deletestudent.html')
    return response

def delete_student(request):
    rno=int(request.GET['rno'])
    try:
        student=Marks.objects.get(rollno=rno)
        student.delete()
        response=render(request,'app1/deletestudent.html',context={"msg":"Deleted successfully...."})
    except:
        response=render(request,'app1/deletestudent.html',context={"msg":"Invalids...."})
    return response

def find_student_temp(request):
    response=render(request,'app1/find.html')
    return response

def find_student(request):
    rno=int(request.GET['rno'])
    try:
        student=Marks.objects.get(rollno=rno)
        result='Pass' if student.sub1 >=40 and student.sub2 >=40 else "Fail"
        response=render(request,'app1/find.html',context={"student":student,'result':result})
    except:
        response=render(request,'app1/find.html',context={"msg":"Invalids...."})
    return response