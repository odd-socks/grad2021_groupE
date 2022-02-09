from dataclasses import field
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'email' , 'address' , 'carry_address','is_carryed',)
        widgets = {'is_carryed': forms.HiddenInput()}
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'email': 'メールアドレス',
            'address' : '住所',
            'carry_address' : '引き受け場所',
            'is_carryed' : '送迎中判定'
        }

class QrFuncForm(forms.Form):
    class Meta:
        model = User
        # lavels = {
        #     'name': '名前',
        #     'email': 'メールアドレス',
        # }
        input_name = forms.CharField()
        input_password = forms.CharField()