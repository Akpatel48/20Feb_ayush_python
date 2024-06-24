from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import *
from django.core.mail import send_mail
import random


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
            error='username or password invalid'
            return render(request,'login.html',{'error':error})
            
    return render(request,'login.html')

def reg(request):
    global otp
    global user
    if request.method=='POST':
        user=re(request.POST)
        if user.is_valid():
            otp=random.randint(111111,999999)
            sub='otp'
            mas=f'your otp is:{otp}'
            from_email='ayushpatel5440@gmail.com'
            to_email=[request.POST['email']]
            print(to_email)
            send_mail(subject=sub,message=mas,from_email=from_email,recipient_list=to_email)
            return redirect('otp')
        else:
            print(user.errors)
            
    return render(request,'reg.html')

def userlogout(request):
    logout(request)
    return redirect('/')

def verifyotp(request):
    global otp
    print(otp)
    if request.method=="POST":
        if request.POST['otp']==str(otp):
            user.save()
            return redirect('login')
    
    return render(request,'otp.html')