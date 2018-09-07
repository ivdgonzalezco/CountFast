from django.db import models

# Create your models here.

class Product(models.Model):

    PRODUCT_STATE = (
        ('A', 'Activate'),
        ('D', 'Deactivate')
    )

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    current_amount = models.IntegerField()
    product_state = models.CharField(max_length=1, choices=PRODUCT_STATE)
    registration_date = models.DateField()


