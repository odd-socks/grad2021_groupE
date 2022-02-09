from django.urls import path
from django.contrib import admin
from . import views

app_name = 'qrfunction'

urlpatterns = [
    path('', views.search, name='search'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('detail/<int:customer_id>/', views.detail, name='detail'),
]