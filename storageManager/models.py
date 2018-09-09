from django.db import models
from django.utils import timezone

# Create your models here.
class Movement (models.Model):
	id_movement = models.IntegerField(default=11)
	id_product = models.IntegerField(default=11)
	quantity = models.IntegerField(default=11)
	id_user_register = models.IntegerField(default=11)
	register_date = models.DateTimeField(null=True)
