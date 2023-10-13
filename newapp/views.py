from django.shortcuts import redirect, render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['emp_id']
    y=request.POST['emp_name']
    z=request.POST['emp_desig']
    mem=Member(emp_id=x,emp_name=y,emp_desig=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['emp_id']
    y=request.POST['emp_name']
    z=request.POST['emp_desig']
    mem=Member.objects.get(id=id)
    mem.emp_id=x
    mem.emp_name=y
    mem.emp_desig=z
    mem.save()
    return redirect("/")
