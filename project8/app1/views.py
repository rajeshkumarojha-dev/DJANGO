from django.shortcuts import render

# Create your views here.
def product(request):
    product_data={"apple":[100,'apple.jpg'],
                  "ball":[101,'ball.jpg'],
                  "dog":[102,'dog.jpg'],
                  "elephant":[103,'elephant.jpg']}
    response=render(request,'app1/index.html',context={'product_data':product_data})
    return response