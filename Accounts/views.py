from django.shortcuts import render,redirect

# Create your views here.


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
         name=request.POST['uname']
         email_id=request.POST['id']
         number=request.POST['no']
         password=request.POST['pass']
         cpass=request.POST['cpass']
        # x=User.objects.create_user(name=name,phone_no=number,email_id=email_id,password=password,cpassword=cpass)
         x.save()
         print("User Craeted")
         return redirect('/home')
    else:
        return render(request, 'registration.html')
   
def login(request):
    return render(request,'login.html')
