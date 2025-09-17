from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Reserva
from .forms import ClienteForm, ReservaForm
from django.db.models import Q

# CRUD Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'reserva/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'reserva/cliente_form.html', {'form': form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'reserva/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'reserva/cliente_confirm_delete.html', {'cliente': cliente})

# CRUD Reserva + Buscador
def reserva_list(request):
    query = request.GET.get('q')
    reservas = Reserva.objects.all()
    if query:
        reservas = reservas.filter(
            Q(cliente__nombre__icontains=query) |
            Q(numero_habitacion__icontains=query)
        )
    return render(request, 'reserva/reserva_list.html', {'reservas': reservas, 'query': query})

def reserva_create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reserva/reserva_form.html', {'form': form})

def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva/reserva_form.html', {'form': form})

def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_list')
    return render(request, 'reserva/reserva_confirm_delete.html', {'reserva': reserva})