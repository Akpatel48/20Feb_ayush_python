from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
    if request.method=='POST':
        req=stunde(request.POST)
        if req.is_valid():
            req.save()
    return render(request,'index.html')

def showdata(request):
    stdata=stundet.objects.all()
    return render(request,'showdata.html',context={'stdata':stdata})

def delete(request,id):
    stid=stundet.objects.get(id=id)
    stundet.delete(stid)
    return redirect('showdata')