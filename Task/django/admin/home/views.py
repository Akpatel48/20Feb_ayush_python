from django.shortcuts import render
from .models import studinfo
from .forms import studinf
# Create your views here.
def index(request):
    if request.method=='POST':
        req=studinf(request.POST)
        if req.is_valid():
            req.save()
            print("Record inserted!")
        else:
            print(req.errors)
    return render(request,'index.html')
def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',context={'stdata':stdata})
    None