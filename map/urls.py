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
#from django.contrib import path
from django.urls import path
from .import views

app_name = 'map'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('login/', views.Login.as_view(), name='login'),#ログイン
    path('logout/', views.Logout.as_view(), name='logout'),#ログアウト
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'), #マイページ
    path('signup/', views.Signup.as_view(), name="signup"),#サインアップ
    path('sign_up_done/', views.SignupDone.as_view(), name="sign_up_done"),#サインアップ完了
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'), # 登録情報の更新

]