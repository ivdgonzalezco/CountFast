from django.contrib import admin
from .models import Post
from .models import DefectiveProducts

# Register your models
admin.site.register(Post)
admin.site.register(DefectiveProducts)