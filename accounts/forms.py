from dataclasses import field
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter


#サインアップフォーム
class CustomSignupForm(SignupForm):
    address = forms.CharField(label='施設住所',max_length=150)

    class Meta:
        model = CustomUser


    def signup(self, request,user):
        user.address = self.cleaned_data['address']
        user.save()
        return user

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args,**kwargs)

    #         self.fields['username'].widget.attrs['class']='form-control'
    #         self.fields['username'].widget.attrs['placeholder']='施設名'

    #         self.fields['email'].widget.attrs['class']='form-control'
    #         self.fields['email'].widget.attrs['placeholder']='メールアドレス'