# from django.contrib import admin
# from .models import (
#     Customer,
#     Product,
#     Cart,
#     OrderPlaced
# )

# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'locality', 'city', 'zipcode', 'state']

# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'product', 'quantity']


# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']



from django.contrib import admin
from .models import Category, Product, Cart, WishList, Order
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Order)
