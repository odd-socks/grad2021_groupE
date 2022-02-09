"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.urls import path,include
from . import views

app_name = 'certification'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),#トップページ
    path('facility/', views.FacilityView.as_view(), name='facility'),#施設ページ
    path('underwriter/', views.UnderwriterView.as_view(), name='underwriter'),#引受人ページ
    path('qr/', views.qrView, name='qr'),#QRコード
]
