from django.shortcuts import render
from .models import *

# Create your views here.


def land(request):
    return render(request, 'land.html', {})


def home(request):
    return render(request, 'home.html', {})


def products(request):

    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})


def customer(request):

    customers = Customer.objects.all()

    return render(request, 'customer.html', {'customers': customers})


def dashboard(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()

    pending = orders.filter(status='Pending').count()

    context = {'products': products, 'customers': customers, 'orders': orders, 'total_orders': total_orders,
               'total_customers': total_customers, 'delivered': delivered, 'pending': pending}

    return render(request, 'dashboard.html', context)
