from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.documento_identidad})"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.CharField(max_length=10)

    def __str__(self):
        return f"Habitación {self.numero_habitacion} - {self.cliente.nombre}"