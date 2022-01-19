from .models import Facility
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


#施設のログインフォーム
class FacilityLoginForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = {'facility_name', 'password',}
        labels = {
            'facility_name':'施設名',
            'password':'パスワード',
            }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FacilityLoginForm, self).__init__(*args, **kwargs)

#施設のサインアップフォーム
class FacilitySignupForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = {'facility_name', 'password', 'address',}
        labels = {
            'facility_name':'施設名',
            'password':'パスワード',
            'address':'住所',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FacilitySignupForm, self).__init__(*args, **kwargs)

#施設情報更新用フォーム
class FacilityUpdateForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = {'facility_name', 'password', 'address',}

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FacilityUpdateForm, self).__init__(*args, **kwargs)

#パスワード変更フォーム
class MyPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PasswordChangeForm, self).__init__(*args, **kwargs)