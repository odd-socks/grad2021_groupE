from django.urls import path
from . import views

app_name = 'user_function'
urlpatterns = [
    path('', views.certification, name="certification"),  # 認証画面用
    path('show_map', views.show_map, name="show_map"),
]
