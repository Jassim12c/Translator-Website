from django import forms

from . import models

class TranslateForm(forms.ModelForm):
    class Meta:
        model = models.Translate
        fields = (
            'sentence',
        )

        widgets = {
            'sentence': forms.TextInput(attrs={'class': 'form-control'}),
        }
