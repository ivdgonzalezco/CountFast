from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.products, name='product_list'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('product/new', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('supplier/', views.suppliers, name='supplier_list'),
    path('supplier/<int:pk>/', views.supplier_details, name='supplier_details'),
    path('supplier/new', views.supplier_new, name='supplier_new'),
    path('supplier/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
]
from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url (r'^user/init_login', views.user_init_login),
    url (r'^user/login', views.user_login),
    url (r'^user/logout', views.user_logout),
    path('main', views.main, name='main'),
    path('user/', views.users, name='user_list'),
    path('user/<int:pk>/', views.user_details, name='user_details'),
    path('user/new', views.user_new, name='user_new'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
]