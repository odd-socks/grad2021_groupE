from django.urls import path
from django.contrib import admin
from . import views
from .views import user_list, user_create,user_update, user_delete

app_name = 'customer'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.toppage, name='toppage'),
    path('index/', views.index, name='index'),
    path("users/", user_list),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    # path("users/<int:user_id>", user_create),
    # path("users/<int:user_id>/update/", user_update),
    # path("users/<int:user_id>/delete/", user_delete),
]