from django.db import models

# Modelo para almacenar la información de los pacientes
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo para almacenar las citas médicas
class Cita(models.Model):

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='citas'
    )

    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Pendiente'
    )

    def __str__(self):
        return f"{self.paciente} - {self.fecha} - {self.estado}"