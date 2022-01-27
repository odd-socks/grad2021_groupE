from django import forms
from .models import User
from .models import GENDER_CHOICES


GENDER_CHOICES = GENDER_CHOICES + [('', '---------')] 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'email' , 'address' , 'carry_address','is_carryed','facility_id')
        widgets = {'is_carryed': forms.HiddenInput()}
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'email': 'メールアドレス',
            'address' : '住所',
            'carry_address' : '引き受け場所',
            'is_carryed' : '送迎中判定',
            'facility_id': '施設_id'
        }

class SubUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'email' , 'address' , 'carry_address','is_carryed','facility_id')
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'email': 'メールアドレス',
            'address' : '住所',
            'carry_address' : '引き受け場所',
            'is_carryed' : '送迎中判定',
             'facility_id': '施設_id'
        }