from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
from curso.models import Curso, Asignacion


# Create your views here.
def curso_nuevo(request):
    if request.method == "POST":

        formulario = CursoForm(request.POST)
        if formulario.is_valid():

         curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])

         for curso_id in request.POST.getlist('alumno'):
             asignacion = Asignacion(alumno_id=alumno_id, curso_id = curso.id)
         asignacion.save()
        messages.add_message(request, messages.SUCCESS, 'CUrso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})