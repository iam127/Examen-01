from django import forms
from .models import Cliente, Reserva

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'documento_identidad']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'fecha_ingreso', 'fecha_salida', 'numero_habitacion']