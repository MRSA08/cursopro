from django import forms
from django.forms import widgets
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese texto aqui'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el subtitulo'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad< 10:
            raise forms.ValidationError('CANTIDAD DEBE SER MAYOR A 10')
        return cantidad