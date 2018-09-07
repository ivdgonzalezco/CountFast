from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.get(id__exact=1)
    return render(request, 'storageManager/product_list.html', {'products': products})