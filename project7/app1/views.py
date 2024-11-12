from django.shortcuts import render

# Create your views here.

def list_student(request):
    student_data={101:["Dhoni","python","Rajesh.jpg"],
                  102:["virat","java","Rajesh (1).png"],
                  103:["rohit","dot net","Rajesh (2).jpg"]}
    response = render(request,"app1/index.html",context={"student_data":student_data})
    return response
