from django.db import models
from django.contrib import admin

# Create your models here.
class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    alumno  = models.ManyToManyField(Alumno, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)