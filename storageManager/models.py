from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.
class Supplier(models.Model):

    SUPPLIER_STATE = (
        ('A', 'Activate'),
        ('D', 'Deactivate')
    )

    nit = models.IntegerField()
    name = models.CharField(max_length=200)
    supplier_state = models.CharField(max_length=1, choices=SUPPLIER_STATE)
    registration_date = models.DateField(default=now().today().date())

class Product(models.Model):

    PRODUCT_STATE = (
        ('A', 'Activate'),
        ('D', 'Deactivate')
    )

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    current_amount = models.IntegerField()
    product_state = models.CharField(max_length=1, choices=PRODUCT_STATE)
    registration_date = models.DateField(default=now().today().date())
    description = models.TextField(default="")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	

class Movement (models.Model):	
	quantity = models.IntegerField()
	id_user_register = models.IntegerField()
	register_date = models.DateTimeField(default=now().today().date())
	id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
	


