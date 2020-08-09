from django import forms
from appModelos.models import *
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion',
                  'precio',
                  'stock',
                  'iva')
        label = {
            'descripcion': 'Nombre Producto',
            'precio': 'Precio',
            'stock': 'Stock',
            'iva':'Iva'}
        widgets={

            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'type':'number',
                    'step':'any',
                    'value':'0',
                    'class': 'form-control'

                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'number'
                }
            ),
            'iva': forms.CheckboxInput(
                attrs={
                    'class': 'field-iva'
                }
            )
        }



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc',
                  'nombre',
                  'direccion',
                  'producto')
        label = {
            'ruc': 'Número de Ruc',
            'nombre': 'Nombre Cliente',
            'direccion': 'Dirección'}
        widgets={

            'ruc':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'direccion': forms.Textarea(
                attrs={
                    'class': 'form-control'

                }
            ),
            'producto': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }