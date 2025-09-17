from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    # Reservas
    path('reservas/', views.reserva_list, name='reserva_list'),
    path('reservas/nuevo/', views.reserva_create, name='reserva_create'),
    path('reservas/editar/<int:pk>/', views.reserva_edit, name='reserva_edit'),
    path('reservas/eliminar/<int:pk>/', views.reserva_delete, name='reserva_delete'),
]