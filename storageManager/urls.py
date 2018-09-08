from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url (r'^users/init_login', views.init_login),
    url (r'^users/login', views.login),
    url (r'^users/logout', views.logout),
    path('main', views.main, name='main'),
    url(r'^users/init_user_registration', views.init_user_registration),
    url(r'^users/register_user', views.register_user),
]