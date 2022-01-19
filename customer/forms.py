from django import forms
from .models import User
 
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'address' , 'carry_address')
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'address' : '住所',
            'carry_address' : '引き受け場所',
        }
        help_texts = {
            'name': '名前を入力',
            'age': '年齢を入力',
            'gender': '性別を選択',
            'address': '住所を入力',
            'carry_address': '送り先住所を入力'
        }