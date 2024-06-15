from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
    user=request.session.get('user')    
    return render(request,'index.html',{'user':user})

def about(request):
    user=request.session.get('user')    
    return render(request,'about.html',{'user':user})

def blog(request):
    user=request.session.get('user')    
    return render(request,'blog.html',{'user':user})

def doctors(request):
    user=request.session.get('user')    
    return render(request,'doctors.html',{'user':user})
def services(request):
    user=request.session.get('user')    
    return render(request,'services.html',{'user':user})

def login(request):
    if request.method=='POST':
        unm=request.POST['unm']
        pas=request.POST['pas']
        user=logi.objects.filter(email=unm,password=pas)
        if user:
            request.session['user']=unm
            return redirect('/')
        else:
            print(user.errors)
    return render(request,'login.html')

def reg(request):
    if request.method=='POST':
        user=re(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
        else:
            print(user.errors)
            
    return render(request,'reg.html')
