from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('',views.index, name="index"),
   path('base/login.html',views.login, name="login"),
   path('base/register.html',views.register, name="register"),
  
]
