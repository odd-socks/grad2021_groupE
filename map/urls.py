from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('map_list/', views.MapListView.as_view(), name="map_list"),
    path('user_list/', views.MapCreateView.as_view(), name="user_list"),
    path('ajax_post_search/', views.MapCreateView.as_view(), name="ajax_post_search"),
]