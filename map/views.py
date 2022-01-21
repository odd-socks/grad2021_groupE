from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView #追加
from django.urls import reverse_lazy #追加 遅延評価用
from .forms import FacilityLoginForm, FacilitySignupForm, FacilityUpdateForm, MyPasswordChangeForm #追加
from django.contrib.auth.mixins import UserPassesTestMixin #追加
from map.models import Facility #モデル情報
from django.shortcuts import redirect, resolve_url #追加
#from django.urls import reverse_lazy
#from django.contrib.auth import login, authenticate #ログイン関数用



# Create your views here.
#トップページ表示
class IndexView(generic.TemplateView):
    template_name = "map/index.html"
#---------------------------------------------------------------

#施設用新規登録機能
class FacilitySignup(generic.CreateView):
    template_name = 'account/facility_form.html'
    form_class = FacilitySignupForm

    #データがポストされた時に呼ばれるメソッド
    def form_valid(self, form):
        facility = form.save() #facility変数にformの情報を保存
        return redirect('map:facility_signup_done')

    #データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "施設登録"
        return context

#施設用新規登録完了表示
class FacilitySignupDone(generic.TemplateView):
    template_name = 'account/facility_signup_done.html'

#----------------------------------------------------

#施設ログイン機能
class FacilityLogin(LoginView):
    form_class = FacilityLoginForm
    template_name = "account/facility_login.html"

    #カスタムログイン関数

    def post(self, request, *arg, **kwargs):
        form = FacilityLoginForm(data=request.POST)
        #データがポストされた場合
        if form.is_valid():
            facility_name = form.cleaned_data.get('facility_name')
            facility = Facility.objects.get(facility_name=facility_name)
            #login(request, facility)#エラー原因-->カスタムログイン関数を使用する
            return redirect('map:index')
        return render(request, 'account/facility_login.html', {'form': form,})

    def get(self, request, *arg, **kwargs):
        form = FacilityLoginForm(request.POST)
        return render(request, 'account/facility_login.html', {'form': form,})
#---------------------------------------------------------------

#施設ログアウト
class FacilityLogout(LogoutView):
    template_name = "account/logout_done.html"

#-----------------------------------------------------------------

#自分しかアクセスできないようにするMixin(My Pageのため)
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']


#施設用マイページ
class FacilityMyPage(OnlyYouMixin,generic.DetailView):
    model = Facility
    template_name = 'account/facility_my_page.html'


#施設登録情報の更新
class FacilityUpdate(OnlyYouMixin, generic.UpdateView):
    model = Facility
    form_class = FacilityUpdateForm
    template_name = 'account/facility_form.html'

    def get_success_url(self):
        return resolve_url('map:facility_my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

#パスワード変更
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('map:password_change_done')
    template_name = 'account/facility_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context

#パスワード変更完了
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'
