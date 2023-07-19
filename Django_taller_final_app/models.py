from django.db import models

class Estado(models.TextChoices):
    RESERVADO = 'RESERVADO', 'Reservado'
    COMPLETADA = 'COMPLETADA', 'Completada'
    ANULADA = 'ANULADA', 'Anulada'
    NO_ASISTEN = 'NO_ASISTEN', 'No Asisten'

class Participantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=15)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=15, choices=Estado.choices, default=Estado.RESERVADO)
    observacion = models.CharField(max_length=50)
