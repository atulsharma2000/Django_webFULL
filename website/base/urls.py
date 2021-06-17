from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('',views.index, name="index"),
   path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('tasks',views.TaskList.as_view(),name='tasks'),
    path('create-task',views.TaskCreate.as_view(),name='task-create'),
]
