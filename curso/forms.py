from django import forms
from .models import Alumno, Curso

class AlumnoForm(forms.ModelForm):
    #todos los campos de Alumno
    class Meta:
        model = Alumno
        fields = ('nombre', 'anio', 'curso')

    def __init__ (self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields["curso"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["curso"].help_text = "Ingrese los curso que tendra el alumno"
        self.fields["curso"].queryset = Curso.objects.all()