from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def view_images(request):
    response = render(request,"app1/imagesview.html")
    return response