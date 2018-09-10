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