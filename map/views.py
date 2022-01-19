from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView #追加
from .forms import FacilityLoginForm #追加

# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
    template_name = "map/index.html"

#施設ログイン
class FacilityLogin(LoginView):
    form_class = FacilityLoginForm
    template_name = "account/facility_login.html"