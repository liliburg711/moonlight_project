from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from florists.models import Florist

# Create your views here.

def index(request):
    products = Product.objects.order_by('-updated').filter(available=True)[:3]

    context = { 
        'products': products 
    }

    return render(request, 'pages/index.html', context)

def brandstory(request):
    florists = Florist.objects.order_by('-hire_date')

    context = {
        'florists' : florists 
    }

    return render(request, 'pages/brandstory.html', context)