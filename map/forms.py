from .models import Facility
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


#施設のログインフォーム
class FacilityLoginForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = {'facility_name', 'password'}
        labels = {
            'facility_name':'施設名',
            'password':'パスワード',
        }

    # def __init__(self, request, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(FacilityLoginForm, self).__init__(*args, **kwargs)
    
   # def __init__(self, *args, **kwargs):
    # super(FacilityLoginForm, self).__init__(*args, **kwargs)
         #htmlの表示を変更可能にします
         #self.fields['facility_name'].widget.attrs['class'] = 'form-control'
         #self.fields['password'].widget.attrs['class'] = 'form-control'
         #self.fields['facility_name'].required = False
         #self.fields['password'].required = False




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



#施設情報更新用フォーム
class FacilityUpdateForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = {'facility_name', 'password', 'address',}


#パスワード変更フォーム
class MyPasswordChangeForm(PasswordChangeForm):

     def __init__(self, *args, **kwargs):
          self.request = kwargs.pop('request', None)
          super(PasswordChangeForm, self).__init__(*args, **kwargs)