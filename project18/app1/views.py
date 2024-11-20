from django.shortcuts import render
from app1.models import Employee
from django.db.models import Sum,Avg,Min,Max
# Create your views here.

def filter_data(request):
    job=request.GET['job'] 
    if job != 'all':   
        qs=Employee.objects.filter(job=job)
    else:   
       qs=Employee.objects.all()

    response=render(request,'app1/show.html',context={"qs":qs})
    return response

def home(request):
    qs=Employee.objects.all()
    response=render(request,'app1/index.html',context={"qs":qs})
    return response

def update_emp(request):
    eno=int(request.GET['eno'])
    usal=float(request.GET['usal'])
    try:
        e=Employee.objects.get(empno=eno)
        e.sal=e.sal+usal
        e.save()
        response=render(request,'app1/update.html',context={"msg":"updated....."})
        return response
    except:
        response=render(request,'app1/update.html',context={"msg":"invalids....."})
        return response
    
def update(request):
    response=render(request,'app1/update.html')
    return response

def aggregate(request):
    sum_salery=Employee.objects.aggregate(Sum('sal'))['sal__sum']
    avg_salery=Employee.objects.aggregate(Avg('sal'))['sal__avg']
    min_salery=Employee.objects.aggregate(Min('sal'))['sal__min']
    max_salery=Employee.objects.aggregate(Max('sal'))['sal__max']
    adict={'sum_salery':sum_salery,'avg_salery':avg_salery,'min_salery':min_salery,'max_salery':max_salery}
    response=render(request,'app1/aggregate.html',context={'adict':adict})
    return response