from django.shortcuts import render, redirect
from django.views import View
<<<<<<< HEAD
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
=======
from .models import *
from django.views.generic import ListView
from .models import Product,Cart,Category,Order,WishList
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
import requests



men = Category.objects.filter(category_for="M")
women = Category.objects.filter(category_for="W")
girls = Category.objects.filter(category_for="G")
boys = Category.objects.filter(category_for="B")


@login_required(login_url='/accounts/')
def products(request):
    products = Product.objects.all()
    context = {
        'items': products,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "home.html", context)

# class HomeView(ListView):
#     model=Item
#     template_name="home-page.html"

@login_required(login_url='/accounts/')
def product(request):
    id = int(request.POST['pid'])-1
    product = Product.objects.get(id = str(id))
    context = {
        'product': product,
        'SG': sunglasses,
        'HB': handbags,
        'E': earrings,
        'B': bracellets,
    }
    return render(request, "product.html", context)
    
@login_required(login_url='/accounts/')
def category_page(request, cid):
    products = Product.objects.filter(category_id = cid)
    context = {
        'products': products,
        'SG': sunglasses,
        'HB': handbags,
        'E': earrings,
        'B': bracellets,
        
    }
    return render(request, "category-page.html", context)

def user_cart(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        if(item.ordered == False):
            total = total + item.price
    context = {
        'items': items, 
        'length': length, 
        'total': total,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "cart.html", context)

def add_to_cart(request):
    user = request.user
    itm = Product.objects.get(id=request.POST.get('pid'))
    item = Cart(user = user, product = itm, quantity = request.POST.get('qty'), size = request.POST.get('size'))
    item.price = int(itm.price) * int(item.quantity)
    item.save()
    return redirect(user_cart)

def remove_from_cart(request):
    cid = request.POST.get('cid')
    cart_item = Cart.objects.get(id = cid)
    cart_item.delete()
    return redirect(user_cart)
>>>>>>> f2a33607885894e69f17c1a48df8467e53d0ce72

def update_cart_item(request):
    ciid = request.POST.get('ciid')
    cart_item = Cart.objects.get(id = ciid)
    cart_item.size = request.POST.get('size')
    cart_item.quantity = request.POST.get('qty')
    cart_item.price = int(cart_item.quantity) * int(cart_item.product.price)
    cart_item.save()
    return redirect(user_cart)

def place_order(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        total = total + item.price
    order = Order(user = user, total_amount = total, address = request.POST.get('address'), address2 = request.POST.get('address2'), country = request.POST.get('country'), state = request.POST.get('state'), pincode = request.POST.get('pincode'))
    order.save()
    for item in items:
        order.products.add(item)
        item.ordered = True
    order.save()
    return redirect(profile_page)

def checkout(request):
    user = request.user
    items = Cart.objects.filter(user = user)
    length = len(items)
    total = 0 
    for item in items:
        if(item.ordered == False):
            total = total + item.price
    context = {
        'user': user,
        'items': items, 
        'length': length, 
        'total': total,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "checkout-page.html", context)

def user_wishlist(request):
    user = request.user
    items = WishList.objects.filter(user = user)
    length = len(items)
    context = {
        'items': items,
        'length': length,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "wishlist-page.html", context)

def add_to_wishlist(request):
    user = request.user
    product = Product.objects.get(id=request.POST.get('pid'))
    item = WishList(user = user, product = product)
    item.save()
    return redirect(user_wishlist)

def remove_from_wishlist(request):
    wid = request.POST.get('wid')
    wishlist_item = WishList.objects.get(id = wid)
    wishlist_item.delete()
    return redirect(user_wishlist)

def profile_page(request):
    orders = Order.objects.filter(user = request.user)
    context = {
        'orders': orders,
        'men': men,
        'women': women,
        'girls': girls,
        'boys': boys,
    }
    return render(request, "profile.html", context)

def product_redirect(request):
    post_data = {'pid': request.POST.get('pid')}
    r = requests.post(request.build_absolute_uri(reverse('product_page')), data = post_data)
    print(r.url)
    return redirect(r)