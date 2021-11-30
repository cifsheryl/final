from django import forms
from .models import Curso, Alumno


class CursoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Curso
        fields = ('nombre', 'anio', 'alumno')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["alumno"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumno"].help_text = "Ingrese los Alumnos que se asignaron al curso"
        self.fields["alumno"].queryset = Alumno.objects.all()