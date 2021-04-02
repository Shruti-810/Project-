from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import random
import string

CATAGORY_CHOICES = {
    ('SG','Sunglasses'),
    ('HB','HandBags'),
    ('E','Earrings'),
    ('B','Bracellets'),
}



# def custom_id(cname, cfor):
#     return ' '.join(map(str,[cfor, cname]))

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_for = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    category_id = models.CharField(primary_key=True, default = " ", max_length=100)

class product(models.Model):
    product_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    image1 = models.CharField(max_length = 1000, default="")
    image2 = models.CharField(max_length = 1000, default="")
    image3 = models.CharField(max_length = 1000, default="")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default="")
    description = models.CharField(max_length = 1000, default="")
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1) 
    price = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Cart)
    ordered_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length = 1000, default="")
    address2 = models.CharField(max_length = 1000, default="")
    country = models.CharField(max_length = 50, default="")
    state = models.CharField(max_length = 50, default="")
    pincode = models.CharField(max_length = 6, default="")
    total_amount = models.IntegerField(default=0)