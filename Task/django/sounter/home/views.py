from django.shortcuts import render
import random
# Create your views here.
nu=0
def indexd(request):
    global nu
    nu+=1
    return render(request, 'index.html',{'num':nu})
def counter(request):
    return render(request,'counte.html')
def about(request):
    return render(request,'about.html')
