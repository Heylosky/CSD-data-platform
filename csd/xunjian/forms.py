from django import forms
from xunjian.models import Xunjian_result
# Create your views here.

class XunjianResultForm(forms.ModelForm):
    class Meta:
        model = Xunjian_result
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)