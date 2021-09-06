from django import forms
from django.forms import widgets

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:

        model = Empleado
        fields = (
            'first_name',
            'second_name',
            'job',
            'departamento',
            'avatar',
            'Habilidades',
        )
        widgets = {
            'Habilidades': forms.CheckboxSelectMultiple()
        }
