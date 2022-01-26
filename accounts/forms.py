from django import forms
from .models import FacilityUser
 
 
class FacilityUserForm(forms.ModelForm):
    class Meta:
        model = FacilityUser
        fields = ('facility_name', 'address' , 'password')
        labels = {
            'facility_name': '施設名',
            'address' : '施設住所',
            'password': 'パスワード',
        }