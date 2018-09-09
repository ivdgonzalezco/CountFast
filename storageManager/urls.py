from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.products, name='product_list'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('product/new', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
]