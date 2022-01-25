from django.urls import path
from django.contrib import admin
from . import views

app_name = 'qrfunction'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('detail/<int:customer_id>/', views.detail, name='detail'),

]