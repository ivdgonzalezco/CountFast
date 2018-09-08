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