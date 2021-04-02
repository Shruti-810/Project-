from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.payment, name='payment-page'),
    path('success', views.success),
    path('debit_success', views.dsuccess),
    path('home', views.home)
]