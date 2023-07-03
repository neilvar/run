from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request, 'index.html',{'result':obj})

# def add(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     s=x+y
#
#     return render(request,"result.html",{'result':s})
