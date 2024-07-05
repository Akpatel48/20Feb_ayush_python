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
        ''' id=logi.objects.filter(email=unm).values('id')
        for i in id:
            id=i
        uid=otp.objects.filter(user_id=id.get('id'))
        print(id.get('id'))
        to_email=[unm]'''
        if user:
            #if uid:
                request.session['user']=unm
                return redirect('/')
                '''else:
                print(to_email)
                getotp(to_email)
                return redirect('otp')'''
        else:
            error='username or password invalid'
            return render(request,'login.html',{'error':error})
            
    return render(request,'login.html')

def reg(request):
    global otp,to_email
    if request.method=='POST':
        user=re(request.POST)
        if user.is_valid():
            to_email=[request.POST['email']]
            email=logi.objects.filter(email=to_email)
            print(to_email)
            if email:
                mass='This email olredi reg goto login'
                return render(request,'reg.html',{'mass':mass})
            else:
                user.save()
                getotp(to_email)
                return redirect('otp')
            
        else:
            print(user.errors)
            
    return render(request,'reg.html')
def getotp(to_email):
    otp=random.randint(111111,999999)
    sub='otp'
    mas=f'your otp is:{otp}'
    from_email='ayushpatel5440@gmail.com'
    send_mail(subject=sub,message=mas,from_email=from_email,recipient_list=to_email)
def userlogout(request):
    logout(request)
    return redirect('/')

def verifyotp(request):
    global otp
    print(otp)
    if request.method=="POST":
        if request.POST['otp']==str(otp):
            return redirect('login')
    id=logi.objects.last()
    #i=logi.objects.filter(id=id)
    
    print(id)
    return render(request,'otp.html',{'id':str(id)[13:-1]}) 