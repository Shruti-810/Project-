from django.contrib import admin
from django.urls import path,include
from Accounts import views


urlpatterns = [
    path('',include('Accounts.urls')),
    path('',include('shop.urls')),
    path('admin/', admin.site.urls),
    
    
]
