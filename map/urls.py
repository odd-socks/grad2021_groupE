from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'map'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),#トップページ
    path('facility_login/', views.FacilityLogin.as_view(), name="facility_login"),#施設用ログインページ
    path('facility_logout/', views.FacilityLogout.as_view(), name='facility_logout'),#施設用ログアウトページ
    path('facility_my_page/<int:pk>/', views.FacilityMyPage.as_view(), name='facility_my_page'),#施設用マイページ
    path('facility_signup/', views.FacilitySignup.as_view(), name='facility_signup'),#サインアップ
    path('facility_signup_done/', views.FacilitySignupDone.as_view(), name='facility_signup_done'),#サインアップ完了
    path('facility_update/<int:pk>', views.FacilityUpdate.as_view(), name='facility_update'),#施設情報の更新
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),#パスワード変更
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),#パスワード変更完了
]