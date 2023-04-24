from .models import Data
from django import forms


class MyForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ("__all__")
