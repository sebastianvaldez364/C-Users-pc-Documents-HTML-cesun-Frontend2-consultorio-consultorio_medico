from django.contrib import admin
from .models import Paciente, Cita


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'edad', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido')


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'fecha', 'hora', 'motivo', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('paciente__nombre', 'paciente__apellido')