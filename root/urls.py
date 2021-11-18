from django.urls import path
from . import views

app_name = 'root'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('map_list/', views.MapListView.as_view(), name="map_list"),
    path('map_list/', views.MapListView.as_view(), name="map_create"),
    path('map_create/', views.MapCreateView.as_view(), name="map_create"),
]