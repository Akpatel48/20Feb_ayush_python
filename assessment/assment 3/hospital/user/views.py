from django.shortcuts import render,redirect
from .froms import *
from django.contrib.auth import logout
# Create your views here.
def index(request):
    sessio=request.session.get('use')
    print(sessio)
    return render(request,'index.html',{'sessio':sessio})
def Doctor(request):
    detil=doctors.objects.all()
    return render(request,'doctor.html',{'detil':detil})
def aboutus(request):
    return render(request,'aboutus.html')
def appointment(request):
    return render(request,'appointment.html')
def sinup(request):
    if request.method=='POST':
        req=logi(request.POST)
        pa=request.POST['password']
        cpa=request.POST['cpassword']
        role=request.POST['role']
        if pa==cpa:
            if req.is_valid():
                req.save()
                if role=='doctor':
                    return redirect('rgistesen')
                else:
                    return redirect('/')
            else:
                print(req.errors)
        else:
            error='password invalid'
            return render(request,'sinup.html',{'error':error})
    return render(request,'sinup.html')
def log(request):
    if request.method=='POST':
        unm=request.POST['user_name']
        pas=request.POST['password']
        use=login.objects.filter(email=unm,password=pas)
        if use:
            request.session['use']=unm
            
            return redirect('/')
        else:
            error='username or password invalid'
            return render(request,'login.html',{'error':error})
            
    return render(request,'login.html')
def form(request):
    if request.method=='POST':
        req=doctor(request.POST)
        if req.is_valid():
            req.save()
        else:
            print(req.errors)
    return render(request,'form.html')
def header(request):
    sessio=request.session.get('use')
    print(sessio)
    return render(request,'header.html',{'sessio':sessio})
def logou(request):
    logout(request)
    return redirect('/')