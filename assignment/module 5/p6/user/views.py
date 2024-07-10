from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def addprodect(request):
    if request.method=='POST':
        req=prodec(request.POST)
        if req.is_valid():
            req.save()
        else:
            print(req.errors)
    return render(request,'add_prodect.html')

def addprodectditel(request):
    prode=prodect.objects.all()
    if request.method=='POST':
        req=sub_prodec(request.POST)
        if req.is_valid():
            req.save()
        else:
            print(req.errors)
    return render(request,'add_prodectditel.html',{'prode':prode})
