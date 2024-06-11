from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['unm']
        pas=request.POST['pas']
        user=re.objects.filter(username=unm,password=pas)
        if user:
            return redirect('home')
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        req=inf(request.POST)
        if req.is_valid():
            req.save()
        else:
            print(req.errors)
    return render(request,'reg.html')
def home(request):
    return render(request,'home.html')
    
    