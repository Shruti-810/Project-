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
 return render(request, 'shop/templates/product.html')

def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(id=prod_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp_amt = (p.quantity * p.product.price)
                amount += temp_amt
            return render(request, 'addtocart.html', {'carts' : cart, 'amount' : amount})
        else:
            return render(request, 'emptycart.html')

def update_cart_item(request):
    cid = request.POST.get('cid')
    cart_item = Cart.objects.get(id = ciid)
    cart_item.quantity = request.POST.get('qty')
    cart_item.price = int(cart_item.quantity) * int(cart_item.product.price)
    cart_item.save()
    return redirect(cart)

def remove_from_cart(request):
    cid = request.POST.get('cid')
    cart_item = Cart.objects.get(id = cid)
    cart_item.delete()
    return redirect(cart)

def buy_now(request):
 return render(request, 'buynow.html')

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
