from django.urls import path
from django.contrib import admin
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'recrues'

urlpatterns = [

    
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='recrues/logged_out.html'), name='logout'),
    path('homepage/', views.homePage, name='homepage'), 
    path('homepage/contactpage/', views.contact_view, name='contactpage'),
    path('homepage/enrollment/', views.subcribe_view, name='enrollment'), 
    path('homepage/listerecrues/', views.list_view, name='listerecrues'),
    path('homepage/enrollment/updateprofile/', views.update_subcribe_view, name='updateprofile'),
]

