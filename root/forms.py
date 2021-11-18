from root.models import Facility, User
from django import forms

class MapCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'