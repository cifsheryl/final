from django.contrib import admin
from curso.models import Curso, CursoAdmin, Alumno, AlumnoAdmin

admin.site.register(Curso, CursoAdmin)
admin.site.register(Alumno, AlumnoAdmin)
