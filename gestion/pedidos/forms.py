from django import forms
from .models import Docente, Curso

class DateInput(forms.DateInput):
    input_type = 'date'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('apellido_paterno','apellido_materno','nombres','fecha_nacimiento','sexo')
        labels = {
            'apellido_paterno': '',
            'apellido_materno': '',
            'nombres': '',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'sexo': ''
        }
        widgets = {
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido materno'}),
            'nombres': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
            'fecha_nacimiento': DateInput,
            'sexo': forms.Select(attrs={'class':'form-control','placeholder': 'Sexo'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre','creditos', 'docente')
        labels = {
            'nombre': '',
            'creditos':'',
            'docente':'',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Curso'}),
            'creditos': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Creditos Academicos'}),
            'docente': forms.Select(attrs={'class':'form-control', 'placeholder': 'docente'}),
        }

