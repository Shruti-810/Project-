from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
class ProductView(View):
    def get(self, request):
        Sunglasses = Product.objects.filter(category='SG')
        HandBags = Product.objects.filter(category='HB')
        Earrings = Product.objects.filter(category='E')
        Bracelets = Product.objects.filter(category='B')
        return render(request, 'Accounts/home.html')
def product(request):
 return render(request, 'app/product.html')

def cart(request):
 return render(request, 'app/cart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

# def address(request):
#  return render(request, 'app/address.html')

# def orders(request):
#  return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/earrings.html')

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

# def checkout(request):
#  return render(request, 'app/checkout.html')
