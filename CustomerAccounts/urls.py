from django.urls import path
from django.contrib import admin
from . import views
from CustomerAccounts import views

app_name = 'CustomerAccounts'

urlpatterns = [
    path('customer_login/', views.CustomerLogin, name='CustomerLogin'),
    path('customer_logout/', views.CustomerLogOut, name='CustomerLogOut'),
    path('customer_login_pass/', views.CustomerLoginPass, name='CustomerLoginPass'),
    path('customer_login_sertif/', views.CustomerLoginSertif, name='CustomerLoginSertif'),
    path('customer_qrcode/', views.CustomerQrcode, name='CustomerQrcode'),
    path('sutomer_routing_maps/', views.CustomerRoutingMaps, name='CustomerRoutingMaps'),
]