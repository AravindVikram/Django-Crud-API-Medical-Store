from .models import Medicine
from django import forms
from django.forms import ModelForm

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = 'name','expiry_date'
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'})
             }


