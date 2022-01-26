from django.urls import path
from django.contrib import admin
from . import views

app_name = 'customer'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.NewFacilityUser, name='create'),
    path('facility_list', views.FacilityUserList, name='facility_list')
]