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
    url (r'^users/init_login', views.init_login),
    url (r'^users/login', views.login),
    url (r'^users/logout', views.logout),
    path('main', views.main, name='main'),
    url(r'^users/init_user_registration', views.init_user_registration),
    url(r'^users/init_user_edition/(?P<user_id>[0-9]+)/$', views.init_user_edition),
    url(r'^users/save_user', views.save_user),
]