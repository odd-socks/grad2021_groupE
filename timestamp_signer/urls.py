from django.urls import path
from timestamp_signer import views

app_name = 'timestamp_signer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #URL生成用
    path('<str:token>/', views.IndexView.as_view(), name='index'),#URL検証用
]