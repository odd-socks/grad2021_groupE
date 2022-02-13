from django import forms
from .models import User
from .models import GENDER_CHOICES


GENDER_CHOICES = GENDER_CHOICES + [('', '---------')] 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'email' , 'address' , 'carry_address','is_carryed','facility_id','map_id','img_name','password')
        
        widgets = {'is_carryed': forms.HiddenInput(),'facility_id': forms.HiddenInput(),'map_id': forms.HiddenInput(),'img_name': forms.HiddenInput(),'password': forms.HiddenInput()}
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'email': 'メールアドレス',
            'address' : '住所',
            'carry_address' : '引き受け場所',
            'is_carryed' : '送迎中判定',
            'facility_id': '施設_id',
            'map_id': '送迎ID',
            'img_name': 'QRコードネーム',
            'password': 'パスワード'

        }


    def __init__(self, *args, **kwargs):
            # for field in self.fields.values():
            #     field.widget.attrs["class"] = "form-control"
            super().__init__(*args,**kwargs)

            self.fields['name'].widget.attrs['class']='form-control'
            self.fields['name'].widget.attrs['placeholder']='(例）山田太郎'

            self.fields['age'].widget.attrs['class']='form-control'
            self.fields['age'].widget.attrs['placeholder']='(例)80'

            self.fields['email'].widget.attrs['class']='form-control'
            self.fields['email'].widget.attrs['placeholder']='(例)taro@taro.com'

            self.fields['address'].widget.attrs['class']='form-control'
            self.fields['address'].widget.attrs['placeholder']='(例)草加駅'

            self.fields['carry_address'].widget.attrs['class']='form-control'
            self.fields['carry_address'].widget.attrs['placeholder']='(例)越谷駅'


class SubUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'age' , 'gender' , 'email' , 'address' , 'carry_address','is_carryed','facility_id','map_id')
        widgets = {'facility_id': forms.HiddenInput(),'map_id': forms.HiddenInput()}
        labels = {
            'name': '名前',
            'age': '年齢',
            'gender' : '性別',
            'email': 'メールアドレス',
            'address' : '住所',
            'carry_address' : '引き受け場所',
            'is_carryed' : '送迎中判定',
            'facility_id': '施設_id',
            'map_id': '送迎ID'
        }

    def __init__(self, *args, **kwargs):
            # for field in self.fields.values():
            #     field.widget.attrs["class"] = "form-control"
            super().__init__(*args,**kwargs)

            self.fields['name'].widget.attrs['class']='form-control'

            self.fields['age'].widget.attrs['class']='form-control'

            self.fields['email'].widget.attrs['class']='form-control'

            self.fields['address'].widget.attrs['class']='form-control'

            self.fields['carry_address'].widget.attrs['class']='form-control'
