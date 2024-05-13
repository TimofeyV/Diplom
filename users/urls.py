from django.urls import path
from django.contrib.auth import views as v
from . import views

urlpatterns = [
    path('login', views.sign_in, name='login'),
    path('register', views.register, name='register'),
    path('logout', v.logout_then_login, name = 'logout'),
]