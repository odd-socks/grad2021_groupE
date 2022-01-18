import imp
from django.views import generic
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model #ユーザーモデル
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import LoginForm, SignupForm,UserUpdateForm, MyPasswordChangeForm
from django.shortcuts import redirect
from django.shortcuts import redirect, resolve_url 
from django.urls import reverse_lazy #遅延評価適用

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

#自分しかアクセスできないようにするMixin(My Pageのため)
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']


#マイページ
class MyPage(OnlyYouMixin, generic.DetailView):
    #model = User
    model = get_user_model()
    template_name = 'account/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される

#サインアップ
class Signup(generic.CreateView):
    template_name = 'account/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('map:sign_up_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

#サインアップ完了
class SignupDone(generic.TemplateView):
    template_name = 'account/sign_up_done.html'

#ユーザー登録情報の更新
class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'account/user_form.html'

    def get_success_url(self):
        return resolve_url('map:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

#パスワード変更
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('map:password_change_done')
    template_name = 'account/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


#パスワード変更完了
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'