from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout


# Create your views here.
def index(request):
    global sessio
    image=img.objects.all()
    sessio=request.session.get('user')
    return render(request,'index.html',{'sessio':sessio,'image':image})

def photodetail(request):
    inc=contact.objects.all()
    for i in inc:
        temp=i.message
        line=temp.split(' ')
    return render(request,'photo-detail.html',{'sessio':sessio})

def about(request):
    return render(request,'about.html',{'sessio':sessio})

def contac(request):
    if request.method=='POST':
        req=inquiry(request.POST)
        if req.is_valid():
            req.save()
    return render(request,'contact.html',{'sessio':sessio})

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        autoh=usinup.objects.filter(email=email,password=password)
        if autoh:
            request.session['user']=email
            return redirect('/')
    return render(request,'login.html',{'sessio':sessio})

def sinup(request):
    if request.method=='POST':
        pho=request.POST['phone']
        ema=request.POST['email']
        phon=usinup.objects.filter(phone=pho)
        emal=usinup.objects.filter(email=ema)
        both=usinup.objects.filter(phone=pho,email=ema)
        if both:
            mass='phone number and email is olredi Registered'
            return render(request,'sinup.html',{'mass':mass})
        elif phon:
            mass='phone number is olredi Registered'
            return render(request,'sinup.html',{'mass':mass})
        elif emal:
            mass='email number is olredi Registered'
            return render(request,'sinup.html',{'mass':mass})
        else:
            req=sinu(request.POST)
            if req.is_valid():
                req.save()
                return redirect('login')
    return render(request,'sinup.html',{'sessio':sessio})

def logogut(request):
    logout(request)
    return redirect('/')