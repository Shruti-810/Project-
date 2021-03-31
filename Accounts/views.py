from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import register
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,r'C:\Users\vrush\Downloads\Online_Shopping_For_Accessories-Project\Online_Shopping_For_Accessories-Project\templates\home.html')

def creation(request):
    if request.method=='POST':
        name=request.POST['uname']
        email_id=request.POST['id']
        number=request.POST['no']
        password=request.POST['pass']
        cpass=request.POST['cpass']

        if User.objects.filter(username=name).exists():
            return HttpResponse("<h1>User Already Exists</h1>")
        if User.objects.filter(email=email_id).exists():
            return HttpResponse("<h1>User Already Exists</h1>")
        if password!=cpass:
            return HttpResponse("<h1>Enter Password Again</h1>")
            
        info=register(name=name,phone_no=number,email_id=email_id,password=password,cpassword=cpass)
        info.save()
        info1=User.objects.create_user(username=name,password=password,email=email_id)
        info1.save()
       
        print("User Created")
        return render(request, r'C:\Users\vrush\Downloads\Online_Shopping_For_Accessories-Project\Online_Shopping_For_Accessories-Project\templates')
    else:
        return render(request, r'C:\Users\vrush\Downloads\Online_Shopping_For_Accessories-Project\Online_Shopping_For_Accessories-Project\Accounts\Accounts')
   
def login(request):
    if request.method=='POST':
        user_login=request.POST['name']
        password_login=request.POST['pass_login']
        user=auth.authenticate(username=user_login,password=password_login)
        if user is not None:
            auth.login(request,user)
            return render(request,r'C:\Users\vrush\Downloads\Online_Shopping_For_Accessories-Project\Online_Shopping_For_Accessories-Project\templates')
        else:
            return HttpResponse("<h1>Invalid User</h1>")
    else:
        return render(request,'login.html')
