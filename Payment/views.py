<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render,redirect

def payment(request):
    if request.method=='POST':
        
    else:
        return render(request,'payment.html')
>>>>>>> Stashed changes
