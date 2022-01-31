from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # 上村設定
    path('admin/', admin.site.urls),
    path('', include('certification.urls')),
    path('accounts/', include('allauth.urls')),
    #下記にaccountsのtemplatesファイルパス記述
    path('accounts/login/', TemplateView.as_view(template_name = 'login.html'), name='login'),
    path('accounts/logout/', TemplateView.as_view(template_name = 'logout.html'), name='logout'),
    path('accounts/signup/', TemplateView.as_view(template_name = 'signup.html'), name='signup'),

    # 水口設定
    path('customer/', include('customer.urls')),  #customer
    path('qrfunction/', include('qrfunction.urls')), #qrfunction

    #古川設定
    path('map/', include('map.urls')),

    #松丸設定
    path('user_function/', include('user_function.urls')),
]
