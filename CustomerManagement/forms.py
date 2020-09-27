from django import forms
from .models import Customer


class CustomerInsertForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = '__all__'