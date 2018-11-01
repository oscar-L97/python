from django import forms
from .models import software, depa

class SwForm(forms.ModelForm):
    class Meta:
        model = software
        fields = ["titulo", "descripcion", "departamento"]

class RawSwForm(forms.Form):
    categories = [
        (None, 'elija un departamento')
    ]

    for dept in depa.objects.all():
        categories.append((dept.nombre, dept.nombre))

    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
    departamento = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categories)

class RawDeptForm(forms.Form):
    nombre = forms.CharField(max_length=50)
