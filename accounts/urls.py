from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home', views.home, name='home'),
    path('products', views.products, name='products'),
    path('customer', views.customer, name='customer'),
    path('dashboard', views.dashboard, name='dashboard'),
]
