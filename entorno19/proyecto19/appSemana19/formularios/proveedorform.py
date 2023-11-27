# En tu archivo forms.py
from django import forms
from ..models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombre', 'telefono']
