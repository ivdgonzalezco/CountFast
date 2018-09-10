from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from storageManager.defective_product_forms import DefectiveProductForm
from .models import DefectiveProducts

def defective_products (request):
    defective_product = DefectiveProducts.objects.all()
    return render(request, 'storageManager/defective_product_list.html', {'defective_products': defective_product})

def defective_product_details(request, pk):
    defective_product = get_object_or_404(DefectiveProducts, pk=pk)
    return render(request, 'storageManager/defective_product_detail.html', {'defective_product': defective_product})

def defective_product_new(request):
    if request.method == "POST":
        form = DefectiveProductForm(request.POST)
        if form.is_valid():
            defective_product = form.save(commit=False)
            defective_product.save()
            return redirect('defective_product_detail', pk=defective_product.pk)
    else:
        form = DefectiveProductForm()
    return render(request, 'storageManager/defective_product_new.html', {'form': form})

def defective_product_edit(request, pk):
    defective_product = get_object_or_404(DefectiveProducts, pk=pk)
    if request.method == "POST":
        form = DefectiveProductForm(request.POST, instance=defective_product)
        if form.is_valid():
            defective_product = form.save(commit=False)
            defective_product.save()
            return redirect('defective_product_details', pk=defective_product.pk)
    else:
        form = DefectiveProductForm(instance=defective_product)
    return render(request, 'storageManager/defective_product_new.html', {'form': form})