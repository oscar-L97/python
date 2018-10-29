from django import forms
from .models import Trabajo

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ["documento", "titulo", "autor"]
