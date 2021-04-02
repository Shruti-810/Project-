
from django.shortcuts import render

from django.shortcuts import render,redirect

def payment(request):
    if request.method=='POST':
        pass
        
    else:
        return render(request,'payment.html')

