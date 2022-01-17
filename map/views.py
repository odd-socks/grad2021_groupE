from django.views import generic
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth import get_user_model
#from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
#トップページ
class IndexView(generic.TemplateView):
    template_name = "map/index.html"

#ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

#ログアウト
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'account/logout_done.html'

