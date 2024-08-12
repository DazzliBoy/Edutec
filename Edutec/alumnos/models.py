from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    nota = models.IntegerField()
    estado = models.CharField(max_length=10, editable=False)

    def save(self, *args, **kwargs):
        self.estado = 'Aprobado' if self.nota >= 14 else 'Desaprobado'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
