from typing import Any, Mapping

from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from . import models

class ConctactForm(forms.ModelForm):
    # CRIA O CAMPO FIRST_NAME MANUALMENTE, SUBSTITUINDO O PADRÃO DO DJANGO
    first_name = forms.CharField( 
        label='Primeiro nome',
        help_text='Digite seu primeiro nome',
        #max_length=100,
        #required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu primeiro nome'
        })
    )
    # CRIA UM CAMPO PERSONALIZADO, QUE NÃO EXISTE NO MODELO, PARA TESTAR A VALIDAÇÃO
    #campo = forms.CharField(
    #    label='Campo personalizado',
    #    help_text='Digite algo',
    #    widget=forms.TextInput(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Campo personalizado'
    #    })
    #)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # SUBSTITUI O WIDGET DO CAMPO FIRST_NAME, ADICIONANDO CLASSES CSS E PLACEHOLDER
        #self.fields['first_name'].widget.attrs.update({
        #    'class': 'form-control',
        #    'placeholder': 'Seu primeiro nome novo'
        #})

    class Meta:
        model = models.Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'show']

        # CRIA NOVO WIDGET PARA O CAMPO FIRST_NAME, SUBSTITUINDO O PADRÃO DO DJANGO
        #widgets = {
        #    'first_name': forms.TextInput(
        #        attrs={
        #            'class': 'form-control',
        #            'placeholder': 'Seu primeiro nome'
        #        }
        #    ),
        #}

    def clean(self):
        cleaned_data = self.cleaned_data 

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        msg = ValidationError(
                'First name igual ao Last name',  
                code='invalid'
            )

        if first_name == last_name:
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()  

    ## VALIDAÇÃO DO CAMPO FIRST_NAME, VERIFICANDO SE O VALOR É 'ABC' E GERANDO UM ERRO DE VALIDAÇÃO SE FOR
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error('first_name', ValidationError(
                'Nome não pode ser ABC',
                code='invalid'
            ))
        return first_name
    

