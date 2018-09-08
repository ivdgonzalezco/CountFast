from django.shortcuts import render
from storageManager.models import User
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import re
# Create your views here.

def init_login(request, message = ""):
    return render_to_response(
        'storageManager/login.html',
        {'message': message}
    )

@csrf_exempt
def login(request):
    user_login = request.POST["user_login"]
    user_password = request.POST["user_password"]

    if len(user_login) == 0 or len(user_password) == 0:
        error_message = "The login and password are required"
    else:
        users = User.objects.filter(login=user_login)
        if users.count() > 0:
            user = users[0]
            if user.password == user_password:
                request.session['current_user_id'] = user.id
                request.session['current_user_name'] = user.name
                request.session['current_user_role'] = user.user_role
                return main(request)
            else:
                error_message = "Wrong password"
        else:
            error_message = "The user does not exist"

    return init_login(request, message=error_message)

@csrf_exempt
def logout(request):
    del request.session['current_user_id']
    del request.session['current_user_name']
    del request.session['current_user_role']
    return init_login(request, message="")

def main(request):
    return render_to_response(
        'storageManager/main.html',
        {'current_user_name': request.session.get('current_user_name'),
         'current_user_role': request.session['current_user_role']}
    )

def init_user_registration(request, message = "", user = {}):
    users = User.objects.all()
    return render_to_response(
        'storageManager/register_user.html',
        {'users': users, 'message': message, 'user': user}
    )

def init_user_edition(request, user_id):
    user = User.objects.get(id = user_id)
    return init_user_registration(request, message="", user = user)

@csrf_exempt
def save_user(request):
    user_id = int(request.POST["user_id"])
    user_name = request.POST["user_name"]
    user_login = request.POST["user_login"]
    user_password = request.POST["user_password"]
    user_role = request.POST["user_role"]
    user_state = request.POST["user_state"]

    if user_id > 0:
        user = User.objects.get(id = user_id)
        user.name = user_name
        user.login = user_login
        user.password = user_password
        user.user_role = user_role
        user.user_state = user_state
    else:
        user = User(
        name=user_name,
        login=user_login,
        password=user_password,
        user_role=user_role,
        user_state=user_state
    )

    if len(user_name) == 0 or len(user_login) == 0 or len(user_password) == 0 or len(user_role) == 0 or len(user_state) == 0:
        return init_user_registration(request, message="All parameters are required. Please verify.", user = user)
    else:
        if user_id > 0:
            users = User.objects.filter(login=user_login).exclude(id = user_id)
        else:
            users = User.objects.filter(login=user_login)

        if users.count() > 0:
            return init_user_registration(request, message="There is already a user with the specified login.", user = user)

        if not is_password_strong(user_password):
            return init_user_registration(request, message="Password validation failed (minlength=8, min one uppercase letter, min one lowercase letter, min one digit).", user = user)

        if user_id > 0:
            user.id = user_id
        user.save()

        return init_user_registration(request, message="User saved successfully.")

def is_password_strong(password):
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')

    return (length_regex.search(password) is not None
            and uppercase_regex.search(password) is not None
            and lowercase_regex.search(password) is not None
            and digit_regex.search(password) is not None)