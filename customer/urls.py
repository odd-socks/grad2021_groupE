from django.urls import path
from django.contrib import admin
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    path('<int:customer_id>', views.detail, name='detail'),
    path('update/<int:customer_id>', views.update, name='update'),
    path('delete/<int:customer_id>', views.delete, name='delete'),
]
