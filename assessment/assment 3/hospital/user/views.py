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
def log(request):
    global unm
    if request.method=='POST':
        unm=request.POST['user_name']
        pas=request.POST['password']
        use=login.objects.filter(email=unm,password=pas)
        doc=doctors.objects.filter(email=unm)
        try:
            role=login.objects.get(email=unm)
            if use:
                request.session['use']=unm
                if role.role=='doctor':
                    if doc:
                        return redirect('/')
                    else:
                        return redirect('rgistesen')
                else:
                    return redirect('/')
        except:
            error='username or password invalid'
            return render(request,'login.html',{'error':error})
            
    return render(request,'login.html')
def aboutus(request):
    return render(request,'aboutus.html',{'sessio':sessio})

def appointment(request):
    sessio=request.session.get('use')
    return render(request,'appointment.html',{'sessio':sessio})

def bookapp(request,id):
    global unm
    sessio=request.session.get('use')
    doctor=doctors.objects.get(id=id)
    time=['10:00','10:30','11:00','11:00','11:30','12:00','04:00','04:30','05:00','05:30','06:00','06:30','07:00']
    if request.method=='POST':
        req=tim(request.POST)
        if req.is_valid:
            req.save()
            print(req.errors)
            return redirect('book_app')
    return render(request,'bookapp.html',{'Doctor':doctor,'sessio':sessio,'time':time}) 
def book_app(request):
    sessio=request.session.get('use')
    if request.method=='POST':
        req=appointen(request.POST)
        if req.is_valid():
            req.save()
            return redirect('appointment')
        else:
            print(req.errors)
    return render(request,'book_appointment.html',{'sessio':sessio})

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
    log=doctor()
    return render(request,'doctor_r.html',{'doc_name':doc_name,'logo':log})
def header(request):
    return render(request,'header.html')
def logou(request):
    logout(request)
    return redirect('/')
