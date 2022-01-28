from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('user_list/'  , views.user_list, name="user_list"  ),
    path('map_list/'   , views.map_list,  name="map_list"   ),
    path('user_search/', views.user_search,        name="user_search"),
    path('map_confirm' , views.map_confirm,        name="map_confirm"),
    path('map_create'  , views.map_create,         name="map_create" ),
]