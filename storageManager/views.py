from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from storageManager.models import Movement
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def links(request):
    return render_to_response('links/list.html')	
	
def new(request):
    return render_to_response('links/form.html')
	
@csrf_exempt
def add(request):
	if request.method == 'POST':
		id_movement = request.POST['idmovement']
		id_product = request.POST['idproduct']
		quantity = request.POST['quantity']
		id_user_register = request.POST['iduserregister']
		register_date = request.POST['registerdate']
		user = User.objects.first()
		movement = Movement.objects.create(
            id_movement=id_movement, 
			id_product=id_product,
			quantity=quantity,
			id_user_register = id_user_register,
			register_date = register_date,		
        )
		movement.save()
		return render_to_response('links/result.html')
	return render_to_response("links/list.html", RequestContext(request, {}))
