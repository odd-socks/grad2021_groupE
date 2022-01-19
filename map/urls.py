from django.urls import path, include
from . import views

app_name = 'map'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),#トップページ
    path('facility_login/', views.FacilityLogin.as_view(), name="facility_login"),#施設用ログインページ
]