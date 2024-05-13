from django.urls import path
from .views import *
from django.conf.urls import include
from catalog.views import product_list

urlpatterns = [
    path('', product_list, name = 'home'),
    path('about', index, name='about'),
    path('delivery', delivery, name='delivery'),
    path('pay', pay, name='pay'),
    path('contacts', contacts, name='contacts')
    
]