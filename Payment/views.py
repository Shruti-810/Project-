
from django.shortcuts import render
from .models import Credit,Debit
from django.shortcuts import render,redirect

def payment(request):
    return render(request,'payment.html')

def success(request):
    email=request.POST['name']
    name=request.POST['id']
    cname=request.POST['cname']
    cno=request.POST['cno']
    cdate=request.POST['date']
    cyear=request.POST['year']
    cvv=request.POST['cvv']
    x=Credit(email=email,name=name,cnumber=cno,cname=cname,cdate=cdate,cyear=cyear,cvv=cvv)
    x.save()
    print('Credited')
    return render(request,'success.html')


def dsuccess(request):
    cname=request.POST['cname']
    cno=request.POST['cno']
    cdate=request.POST['cdate']
    cyear=request.POST['cyear']
    cvv=request.POST['cvv']
    x=Debit(dnumber=cno,dname=cname,ddate=cdate,dyear=cyear,debit_cvv=cvv)
    x.save()
    print('Debited')
    return render(request,'success.html')


def home(request):
    return render(request, r'C:\Users\Arun\Desktop\Sem 4\SP\Django\Online_Shopping_For_Accessories\templates\home.html')