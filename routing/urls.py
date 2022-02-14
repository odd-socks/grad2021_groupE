from django.urls import path
from . import views
# from .views import delete

app_name = 'routing'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('user_list/', views.user_list, name="user_list"),
    path('routing_list/', views.routing_list, name="routing_list"),
    path('user_search/', views.user_search, name="user_search"),
    path('confirm/', views.confirm, name="confirm"),
    path('create/', views.create, name="create"),
    path('delete/<int:route_id>/', views.delete, name="delete"),
]