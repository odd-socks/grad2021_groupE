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
        #fields = ("username","email","address")


    def signup(self, request,user):
        user.address = self.cleaned_data['address']
        user.save()
        return user