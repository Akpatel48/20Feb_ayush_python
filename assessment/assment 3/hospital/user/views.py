from django.shortcuts import render,redirect
from .froms import *
from django.contrib.auth import logout
# Create your views here.
'''def index(request):
    global sessio
    sessio=request.session.get('use')
    role=login.objects.values_list('role')
    print(role)
    #role=request.login.get()
    return render(request,'index.html',{'sessio':sessio,'role':role})'''

def index(request):
    global sessio
    
    sessio=request.session.get('use')
    detil=doctors.objects.all()
    return render(request,'index.html',{'detil':detil,'sessio':sessio})

def aboutus(request):
    return render(request,'aboutus.html',{'sessio':sessio})

def appointment(request):
    return render(request,'appointment.html',{'sessio':sessio})

def bookapp(request,id):
    doctor=doctors.objects.get(id=id)
    return render(request,'bookapp.html',{'Doctor':doctor}) 
def book_app(request):
    if request.method=='POST':
        req=appointen(request.POST)
        if req.is_valid():
            req.save()
        else:
            print(req.errors)
    return render(request,'book_appointment.html')

def sinup(request):
    if request.method=='POST':
        req=logi(request.POST)
        pa=request.POST['password']
        cpa=request.POST['cpassword']
        role=request.POST['role']
        if pa==cpa:
            if req.is_valid():
                req.save()
                return redirect('login')
            else:
                print(req.errors)
        else:
            error='password invalid'
            return render(request,'sinup.html',{'error':error})
    return render(request,'sinup.html')
def log(request):
    global unm
    if request.method=='POST':
        unm=request.POST['user_name']
        pas=request.POST['password']
        use=login.objects.filter(email=unm,password=pas)
        print(unm)
        role=login.objects.get(email=unm)
        print(role.role)
        if use:
            request.session['use']=unm
            if role.role=='doctor':
                return redirect('rgistesen')
            else:
                return redirect('/')
        
        else:
            error='username or password invalid'
            return render(request,'login.html',{'error':error})
            
    return render(request,'login.html')
def doctor_r(request):
    print(unm)
    doc_name=login.objects.get(email=unm)
    print(doc_name)
    if request.method=='POST':
        req=doctor(request.POST)
        if req.is_valid():
            req.save()
            return redirect('/')
        else:
            print(req.errors)
    return render(request,'doctor_r.html',{'doc_name':doc_name})
def header(request):
    return render(request,'header.html')
def logou(request):
    logout(request)
    return redirect('/')
