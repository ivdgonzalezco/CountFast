URLS

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('defective_product/', views.defective_products(), name='defective_product_list'),
    path('defective_product/<int:pk>/', views.defective_product_details, name='defective_product_detail'),
    path('defective_product/new', views.defective_product_new, name='defective_product_new'),
    path('defective_product/<int:pk>/edit/', views.defeproduct_edit, name='defective_product_edit'),
]
