from map.models import Facility, User
from django import forms

class MapCreateForm(forms.Form):
     name = forms.CharField(label='名前',max_length=50)
     facility = forms.IntegerField(label='施設番号')

     def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)