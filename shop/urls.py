#from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.ProductView.as_view(), name="home"),
    path('cart/', views.add_to_cart, name=' My Cart'),
    # path('earrings/', views.mobile, name='earrings'),
    # # path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product, name='product')
    # path('buy_now/', views.product_detail, name='buy_now')
    

    
]
