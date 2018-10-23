from django import forms

from .models import Tweet

class FormCreate(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["content"]
