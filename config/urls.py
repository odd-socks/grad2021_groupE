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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('accounts/', include('allauth.urls')),

    path('accounts/login/', TemplateView.as_view(template_name = 'login.html'), name='login'),
    path('accounts/logout/', TemplateView.as_view(template_name = 'logout.html'), name='logout'),
    path('accounts/logout_done/', TemplateView.as_view(template_name = 'logout_done.html'), name='logout_done'),
    path('accounts/signup/', TemplateView.as_view(template_name = 'signup.html'), name='signup'),
    path('accounts/sign_up_done/', TemplateView.as_view(template_name = 'sign_up_done.html'), name='sign_up_done'),
    path('accounts/my_page/', TemplateView.as_view(template_name = 'my_page.html'), name='my_page'),
    path('accounts/my_pate/', TemplateView.as_view(template_name = 'my_pate.html'), name='my_pate'),
    path('accounts/password_change/', TemplateView.as_view(template_name = 'password_change.html'), name='password_change'),
    path('accounts/user_form/', TemplateView.as_view(template_name = 'user_form.html'), name='user_form'),






]