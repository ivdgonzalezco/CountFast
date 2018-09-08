from django.db import models
from django.utils.timezone import now

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





class User(models.Model):

    USER_ROLE = (
        ('A', 'Administrator'),
        ('E', 'Employee')
    )

    USER_STATE = (
        ('A', 'Activate'),
        ('D', 'Deactivate')
    )

    name = models.CharField(max_length=100)
    user_role = models.CharField(max_length=1, choices=USER_ROLE)
    user_state = models.CharField(max_length=1, choices=USER_STATE)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
