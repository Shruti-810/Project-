from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import register
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'home.html')

def creation(request):
    if request.method=='POST':
        name=request.POST['uname']
        email_id=request.POST['id']
        number=request.POST['no']
        password=request.POST['pass']
        cpass=request.POST['cpass']
        info=register(name=name,phone_no=number,email_id=email_id,password=password,cpassword=cpass)
        info.save()
        print("User Created")
        return render(request, r'C:\Users\Arun\Desktop\Sem 4\SP\Django\Online_Shoping_For_Accessories\templates\home.html')
    else:
        return render(request, r'C:\Users\Arun\Desktop\Sem 4\SP\Django\Online_Shoping_For_Accessories\Accounts\Accounts\registration.html')
   
def login(request):
    if request.method=='POST':
        email=request.POST['id']
        password=request.POST['pass']
        return render(request, r'C:\Users\Arun\Desktop\Sem 4\SP\Django\Online_Shoping_For_Accessories\templates\home.html')
    else:
        return render(request,'login.html')
