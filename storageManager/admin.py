from django.contrib import admin
from .models import DefectiveProducts
from .models import User
from .models import Product

# Register your models

admin.site.register(DefectiveProducts)
admin.site.register(User)
admin.site.register(Product)