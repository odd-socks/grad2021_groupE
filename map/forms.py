from .models import Facility
from django import forms

#施設のログインフォーム
class FacilityLoginForm(forms.ModelForm):
    #facility_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'施設名'}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'パスワード'}))
    
    class Meta:
        model = Facility
        fields = {'facility_name', 'password',}
        labels = {
            'facility_name':'施設名',
            'password':'パスワード'
            }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FacilityLoginForm, self).__init__(*args, **kwargs)

