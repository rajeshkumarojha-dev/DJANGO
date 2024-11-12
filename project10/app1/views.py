from django.shortcuts import render

# Create your views here.
def filter(request):
    num=45
    response = render(request,'app1/filter.html',context={'num':num})
    return response