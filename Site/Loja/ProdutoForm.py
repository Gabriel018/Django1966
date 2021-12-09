
from .models import Produto
from django import forms

class Formulario_Produto(forms.ModelForm):
    class Meta:
        model = Produto

        fields = {
            'titulo',
            'desc',
            'price',
        }

