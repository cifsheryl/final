from django.shortcuts import render
from django.contrib import messages
from .forms import AlumnoForm
from curso.models import Alumno, Actuacion, AlumnoAdmin

def curso_nuevo(request):
    if request.method == "POST":
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            alumno = Alumno.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for curso_id in request.POST.getlist('curso'):
                actuacion = Actuacion(curso_id=curso_id, alumno_id = alumno.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Alumno Guardado Exitosamente')
    else:
        formulario = AlumnoForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})
