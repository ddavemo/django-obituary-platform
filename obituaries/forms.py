from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
        }
