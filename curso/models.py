from django.db import models
from django.contrib import admin

# Create your models here.
class Curso(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    curso   = models.ManyToManyField(Curso, through='Actuacion')

    def __str__(self):
        return self.nombre

class Actuacion (models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):
    model = Actuacion
#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.
    extra = 1


class CursoAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class AlumnoAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)