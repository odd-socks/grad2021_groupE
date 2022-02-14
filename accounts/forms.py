from dataclasses import field
from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm

from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter


#サインアップフォーム
class CustomSignupForm(SignupForm):
    address = forms.CharField(label='施設住所',max_length=150)

    class Meta:
        model = CustomUser
        fields = ('username', 'email' , 'address' , 'password1')
        labels = {
            'id_username': '施設名',
            'id_email':'メール',
            'id_address':'施設住所',
            'id_password1':'パスワード'
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['username'].widget.attrs['placeholder']='(例)大原老人ホーム'

            self.fields['email'].widget.attrs['class']='form-control'
            self.fields['email'].widget.attrs['placeholder']='(例)test@test.com'

            self.fields['address'].widget.attrs['class']='form-control'
            self.fields['address'].widget.attrs['placeholder']='(例)埼玉県越谷市北越谷2-34-1'

            self.fields['password1'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['placeholder']='(例)パスワード'



    def signup(self, request, user):
        user.address = self.cleaned_data['address']
        user.save()
        return user


#ログイン
class CustomLoginForm(LoginForm):
    # address = forms.CharField(label='施設住所',max_length=150)

    class Meta:
        model = CustomUser
        fields = ('login', 'password')
        labels = {
            'login': '施設名',
            'password':'パスワード',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            self.fields['login'].widget.attrs['class']='form-control'
            self.fields['login'].widget.attrs['placeholder']='(例)大原老人ホーム'

            self.fields['password'].widget.attrs['class']='form-control'
            self.fields['password'].widget.attrs['placeholder']='(例)パスワード'


    def login(self, request, user):
        # user.address = self.cleaned_data['address']
        user.save()
        return user