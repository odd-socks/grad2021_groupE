from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('map_list/', views.MapListView.as_view(), name="map_list"),
    path('user_list/', views.UserList.as_view(), name="user_list"),
    path('ajax_post_search/', views.ajax_post_search, name="ajax_post_search"),
    # path('ajax_map_create/', views.ajax_map_create, name="ajax_map_create"),
]