from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/home.html', views.home, name='home'),
    path('home/Personal_Protective_Equipment/ppe.html', views.ppe, name="ppe"),
   
]