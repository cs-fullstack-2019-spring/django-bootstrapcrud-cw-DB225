from django import forms
from .models import GarageModel


class GarageForm(forms.ModelForm):
    class Meta:
        model = GarageModel
        fields = '__all__'
