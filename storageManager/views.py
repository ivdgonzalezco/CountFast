from django.shortcuts import render
from storageManager.models import User
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def init_login(request, message = ""):
    #users = User.objects.get(id__exact=1)
    return render_to_response(
        'storageManager/login.html',
        {'message': message}
    )

@csrf_exempt
def login(request):
    errorMessage = ""
    user_login = request.POST["user_login"]
    user_password = request.POST["user_password"]

    if len(user_login) == 0 or len(user_password) == 0:
        errorMessage = "The login and password are required"
    else:
        users = User.objects.filter(login=user_login)
        if users.count() > 0:
            user = users[0]
            if user.password == user_password:
                request.session['current_user_id'] = user.id
                request.session['current_user_name'] = user.name
                request.session['current_user_role'] = user.user_role
                return render(request, 'storageManager/main.html')
            else:
                errorMessage = "Wrong password"

    return init_login(request, message=errorMessage)

@csrf_exempt
def logout(request):
    request.session.clear()
    return init_login(request, message="")

def main(request):
    return render_to_response(
        'storageManager/main.html'
    )

def init_user_registration(request, message = ""):
    users = User.objects.all()
    return render_to_response(
        'storageManager/register_user.html',
        {'users': users, 'message': message}
    )

@csrf_exempt
def register_user(request):
    user_name = request.POST["user_name"]
    user_login = request.POST["user_login"]
    user_password = request.POST["user_password"]
    user_role = request.POST["user_role"]
    user_state = request.POST["user_state"]

    if len(user_name) == 0 or len(user_login) == 0 or len(user_password) == 0 or len(user_role) == 0 or len(user_state) == 0:
        return init_user_registration(request, message="All parameters are required. Please verify.")
    else:
        user = User(
            name = user_name,
            login = user_login,
            password = user_password,
            user_role = user_role,
            user_state = user_state
        )
        user.save()

        return init_user_registration(request, message="User saved successfully.")

