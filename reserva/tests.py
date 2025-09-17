from django.test import TestCase
from django.urls import reverse
from .models import Cliente

class ReservaFormViewTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Carlos Test", documento_identidad="11122233")

    def test_reserva_form_muestra_clientes(self):
        response = self.client.get(reverse('reserva_create'))
        self.assertContains(response, "Carlos Test")