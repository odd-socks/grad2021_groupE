from django.urls import path
from . import views

app_name = 'root'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    # path('map_create/', views.MapCreateView.as_view(), name="map_create"),
    path('user_list/', views.UserListView.as_view(), name="user_list"),
    path('user_list_ajax/', views.UserJsonView.as_view(), name="userlist_ajax"),
]