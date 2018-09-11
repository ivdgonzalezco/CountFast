from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from .user_forms import UserForm
from .models import User, Product, Supplier, Move
from .supplier_forms import SupplierForm
from .product_forms import ProductForm
from .move_forms import MoveForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from storageManager.defective_product_forms import DefectiveProductForm
from .models import DefectiveProducts
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


def user_init_login(request, message = ""):
    return render_to_response(
        'storageManager/login.html',
        {'message': message}
    )

@csrf_exempt
def user_login(request):
    login = request.POST["user_login"]
    password = request.POST["user_password"]

    if len(login) == 0 or len(password) == 0:
        error_message = "The login and password are required"
    else:
        user_list = User.objects.filter(login=login)
        if user_list.count() > 0:
            user = user_list[0]
            if user.password == password:
                request.session['current_user_id'] = user.id
                request.session['current_user_name'] = user.name
                request.session['current_user_role'] = user.user_role
                return main(request)
            else:
                error_message = "Wrong password"
        else:
            error_message = "The user does not exist"

    return user_init_login(request, message=error_message)

@csrf_exempt
def user_logout(request):
    del request.session['current_user_id']
    del request.session['current_user_name']
    del request.session['current_user_role']
    return user_init_login(request, message="")

def main(request):
    return render_to_response(
        'storageManager/main.html',
        {'current_user_name': request.session['current_user_name'],
         'current_user_role': request.session['current_user_role']}
    )

def users(request):
    user_list = User.objects.all()
    return render(request, 'storageManager/user_list.html', {'users': user_list})

def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'storageManager/user_details.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'storageManager/user_new.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'storageManager/user_new.html', {'form': form})


def moves(request):
    movement = Move.objects.all()
    product = Product.objects.all()
    return render(request, 'storageManager/move_list.html', {'moves': movement, 'products': product})


def move_new(request):
    if request.method == "POST":
        form = MoveForm(request.POST)
        if form.is_valid():
            move = form.save(commit=False)
            product = get_object_or_404(Product, pk=move.product.pk)
            if move.move_state == 'I':
                product.current_amount = F('current_amount') + move.quantity
            else:
                product.current_amount = F('current_amount') - move.quantity
            product.save()
            move.save()
            return redirect('move_details', pk=move.pk)
    else:
        form = MoveForm()
    return render(request, 'storageManager/move_new.html', {'form': form})


def move_details(request, pk):
    move = get_object_or_404(Move, pk=pk)
    return render(request, 'storageManager/move_details.html', {'move': move})

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
            product = get_object_or_404(Product, pk=defective_product.product.pk)
            product.current_amount = F('current_amount') - defective_product.quantity
            product.save()
            defective_product.save()
            return redirect('defective_product_details', pk=defective_product.pk)
    else:
        form = DefectiveProductForm(instance=defective_product)
    return render(request, 'storageManager/defective_product_new.html', {'form': form})