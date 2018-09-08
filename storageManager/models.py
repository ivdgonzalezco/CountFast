from django.db import models

from django.utils import timezone

# Create your models here.
class DefectiveProducts(models.Model):
    id = models.AutoField(primary_key=True)
    # id_product = models.ForeignKey('product.__', on_delete=models.CASCADE)
    id_product = models.IntegerField()
    id_registration_user = models.IntegerField()
    quantity = models.IntegerField()
    registration_date = models.DateTimeField(blank=True, null=True)
    failed_description = models.TextField()

    def __str__(self):
        return self.failed_description

#Agregar el nombre del producto
