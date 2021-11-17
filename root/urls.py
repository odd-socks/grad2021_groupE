from django.urls import path
from . import views
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Facility, User

app_name = 'root'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('map_select/', views.MapSelectView.as_view(), name="map_select"),
    path('map_create/', views.MapCreateView.as_view(), name="map_create"),
]