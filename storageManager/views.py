from django.shortcuts import render, redirect, get_object_or_404
from .product_forms import ProductForm
from .supplier_forms import SupplierForm
from .models import Product, Supplier

def products(request):
    product = Product.objects.all()
    return render(request, 'storageManager/product_list.html', {'products': product})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'storageManager/product_details.html', {'product': product})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_details', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'storageManager/product_new.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_details', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'storageManager/product_new.html', {'form': form})

def suppliers(request):
    supplier = Supplier.objects.all()
    return render(request, 'storageManager/supplier_list.html', {'suppliers': supplier})

def supplier_details(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'storageManager/supplier_details.html', {'supplier': supplier})

def supplier_new(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            return redirect('supplier_details', pk=supplier.pk)
    else:
        form = SupplierForm()
    return render(request, 'storageManager/supplier_new.html', {'form': form})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.save()
            return redirect('supplier_details', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'storageManager/supplier_new.html', {'form': form})
