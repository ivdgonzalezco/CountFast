from django.shortcuts import render, redirect, get_object_or_404
from .user_forms import UserForm
from .models import User
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

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
