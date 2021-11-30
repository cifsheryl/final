from django.contrib import admin

# Register your models here.

from curso.models import Alumno, AlumnoAdmin, Curso, CursoAdmin
#Registramos nuestras clases principales.

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso, CursoAdmin)