from django import forms
from Apps.NoticiasCRUD.models import *

class NoticiasCrearForm(forms.ModelForm):
    class Meta:
        model = NoticiasModelo

        fields=[
            'titulo',
            'fecha',
            'resumen',
            'detalle',
            'tipo',
        ]

        labels={
            'titulo':'Titulo',
            'fecha':'Fecha',
            'resumen':'Resumen',
            'detalle':'Detalle',
            'tipo':'Tipo',
        }

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
            'resumen':forms.Textarea(attrs={'class':'form-control'}),
            'detalle':forms.Textarea(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
        }
