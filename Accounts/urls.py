from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('registration', views.creation, name="register_page"),
    path('login' , views.login, name="login_page"),
]




