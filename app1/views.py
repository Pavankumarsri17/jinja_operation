from django.http import request
from django.shortcuts import render

# Create your views here.
def jinja_operation(request):
    d={'a':100,'name':'pavan'}
    return render(request,'h1.html',context=d)
