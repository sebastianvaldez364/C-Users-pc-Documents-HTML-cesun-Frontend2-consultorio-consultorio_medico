from django.shortcuts import render, get_object_or_404
from .models import Paciente, Cita


# Página principal del consultorio
def inicio(request):
    total_pacientes = Paciente.objects.count()
    total_citas = Cita.objects.count()
    citas_pendientes = Cita.objects.filter(estado='Pendiente').count()

    contexto = {
        'total_pacientes': total_pacientes,
        'total_citas': total_citas,
        'citas_pendientes': citas_pendientes,
    }

    return render(request, 'citas/inicio.html', contexto)


# Mostrar todos los pacientes registrados
def lista_pacientes(request):
    pacientes = Paciente.objects.all()

    return render(request, 'citas/pacientes.html', {
        'pacientes': pacientes
    })


# Mostrar la información y las citas de un paciente
def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    citas = paciente.citas.all()

    return render(request, 'citas/detalle_paciente.html', {
        'paciente': paciente,
        'citas': citas
    })


# Mostrar todas las citas médicas
def lista_citas(request):
    citas = Cita.objects.select_related('paciente').all()

    return render(request, 'citas/citas.html', {
        'citas': citas,
        'titulo': 'Todas las citas médicas'
    })


# Mostrar únicamente las citas pendientes
def citas_pendientes(request):
    citas = Cita.objects.filter(
        estado='Pendiente'
    ).select_related('paciente')

    return render(request, 'citas/citas.html', {
        'citas': citas,
        'titulo': 'Citas pendientes'
    })