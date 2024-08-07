from django.shortcuts import render,redirect
from .froms import *
from django.contrib.auth import logout
# Create your views here.

#index 
def index(request):
    session=request.session.get('use')
    detil=doctors.objects.all()
    try:
        role=login.objects.get(email=session)
    except:
        return render(request,'index.html',{'detil':detil})
    try:
        return render(request,'index.html',{'detil':detil,'sessio':session,'role':role})
    except:
        return render(request,'index.html',{'detil':detil})
        

#sinup 
def sinup(request):
    if request.method=='POST':
        req=loginform(request.POST)
        pa=request.POST['password']
        cpa=request.POST['cpassword']
        email=request.POST['email']
        emai=login.objects.filter(email=email)
        if emai:
            mass='your email olredi registerd'
            return render(request,'sinup.html',{'mass':mass})     
        else:
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

#login 
def loginview(request):
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

#check appointment view
def appointment(request):
    session=request.session.get('use')
    ditle=appointments.objects.filter(user=session)
    try:
        role=login.objects.get(email=session)
    except:
        return render(request,'appointment.html',{'sessio':session,'ditle':ditle})
    return render(request,'appointment.html',{'sessio':session,'ditle':ditle,'role':role})

#appointment psante ditle get
def book_app(request):
    session=request.session.get('use')
    doctor=doctors.objects.all()
    time=['10:00','10:30','11:00','11:00','11:30','12:00','04:00','04:30','05:00','05:30','06:00','06:30','07:00']
    if request.method=='POST':
        req=appointenform(request.POST)
        if req.is_valid():
            req.save()
            return redirect('appointment')
        else:
            print(req.errors)
    try:
        role=login.objects.get(email=session)
    except:
        return render(request,'book_appointment.html',{'Doctor':doctor,'sessio':session,'time':time})
    return render(request,'book_appointment.html',{'Doctor':doctor,'sessio':session,'time':time,'role':role})

#doctor ditle get
def doctor_r(request):
    session=request.session.get('use')
    doc_name=login.objects.get(email=session)
    if request.method=='POST':
        req=doctorsform(request.POST,request.FILES)
        if req.is_valid():
            req.save()
            return redirect('/')
        else:
            print(req.errors)
    log=doctors()
    return render(request,'doctor_r.html',{'doc_name':doc_name,'logo':log})

def doctor(request):
    session=request.session.get('use')
    docto=doctors.objects.all()
    try:
        role=login.objects.get(email=session)
        
    except: 
        return render(request,'doctor.html',{'sessio':session})
    return render(request,'doctor.html',{'sessio':session,'role':role,'docto':docto})

def deletedata(request,id):
    stid=doctors.objects.get(id=id)
    #doctors.delete(stid)
    return redirect('doctor')

#logout
def logou(request):
    logout(request)
    return redirect('/')

#about 
def aboutus(request):
    session=request.session.get('use')
    return render(request,'aboutus.html',{'sessio':session})
