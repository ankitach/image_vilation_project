from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home.html', views.home, name='home'),
    path('Personal_Protective_Equipment/ppe.html', views.ppe, name="ppe")
]