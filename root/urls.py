from django.urls import path
from . import views

app_name = 'root'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
]