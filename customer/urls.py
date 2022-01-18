from django.urls import path
from django.contrib import admin
from . import views
from .views import user_list, user_create,user_update, user_delete

app_name = 'customer'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("users/", user_list),
    path("users/<int:user_id>", user_create),
    path("users/<int:user_id>/update/", user_update),
    path("users/<int:user_id>/delete/", user_delete),
]