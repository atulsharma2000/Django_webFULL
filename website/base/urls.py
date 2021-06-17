from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('',views.index, name="index"),
   path('login/',views.login, name="login"),
   path('register/',views.RegisterPage.as_view(), name="register"),
  
]
