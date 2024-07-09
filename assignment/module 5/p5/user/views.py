from django.shortcuts import render,redirect
from .froms import *
# Create your views here.
def index(request):
    if request.method=='POST':
        req=userdata(request.POST)
        if req.is_valid():
            req.save()    
    return render(request,'index.html')
def view(request):
    show=data.objects.all()
    
    return render(request,'view.html',{'show':show})
def update(request,id):
    stid = data.objects.get(id=id)
    if request.method == 'POST':
        stdata=userdata(request.POST,instance=stid)
        if stdata.is_valid():
            stdata.save()
            return redirect('view')
        else:
            print(stdata.errors)
    else:
        stdata = userdata(instance=stid)
    return render(request,'update.html',{'stid':stid})
def delete(request,id):
    stid = data.objects.get(id=id)
    data.delete(stid)
    return redirect('view')