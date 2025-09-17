# Gestor de Reservas de Hotel

Este proyecto es una aplicación web desarrollada en Django para la gestión de reservas de hotel y sus clientes.

## Características

- CRUD de Clientes (crear, listar, editar, eliminar)
- CRUD de Reservas (crear, listar, editar, eliminar)
- Relación entre reservas y clientes
- Buscador de reservas por cliente o número de habitación
- Interfaz web sencilla (puedes mejorarla con Bootstrap)

## Requisitos

- Python 3.8+
- Django 4.x o superior

## Instalación

1. Clona el repositorio o descarga el código.
2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Instala las dependencias:
    ```bash
    pip install django
    ```
4. Aplica las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

- Accede a `http://127.0.0.1:8000/clientes/` para gestionar clientes.
- Accede a `http://127.0.0.1:8000/reservas/` para gestionar reservas.

## Estructura de Carpetas

```
hotel/
    settings.py
    urls.py
reserva/
    models.py
    views.py
    forms.py
    urls.py
    templates/
        reserva/
            cliente_list.html
            cliente_form.html
            reserva_list.html
            reserva_form.html
manage.py
```

## Pruebas

Para ejecutar los tests:
```bash
python manage.py test reserva
```
