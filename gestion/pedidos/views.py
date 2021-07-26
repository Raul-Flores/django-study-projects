from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import CursoForm, DocenteForm
from .models import Curso, Docente
from django.contrib import messages
# Create your views here.
#Vistas docentes *CRUD
@login_required
def docentes(request):
    if request.method == 'GET':
            form = DocenteForm()
            contexto = {
              'form':form
            }
    else:
        form = DocenteForm(request.POST)
        contexto = {
          'form':form
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Docente Agregado")
            return redirect('docentes')
    return render(request,'docentes.html', contexto)
@login_required
def listado_docentes(request):
  docentes = Docente.objects.all()
  print (docentes)
  if request.method == 'GET':
        contexto = {
          'docente': docentes
        }
  return render(request,'listado_docentes.html', contexto)
@login_required
def eliminardocente(request, id):
    devices = Docente.objects.get(id = id)
    devices.delete()
    return redirect('listado_docentes')
@login_required
def editardocente(request,id):
    docente = Docente.objects.get(id = id)
    if request.method =='GET':
        form = DocenteForm(instance = docente)
        contexto = {
            'form': form
        }
    else:
        form = DocenteForm(request.POST, instance = docente)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('docente')
    return render(request, 'docentes.html', contexto)
#Vistas cursos *CRUD
@login_required
def cursos(request):
    if request.method == 'GET':
        form = CursoForm()
        contexto = {
          'form':form
        }
    else:
        form = CursoForm(request.POST)
        contexto = {
          'form':form
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Registro Agregado")
            return redirect('cursos')
    return render(request,'cursos.html', contexto)
@login_required
def listado_cursos(request):
  cursos = Curso.objects.all()
  print (cursos)
  if request.method == 'GET':
        contexto = {
          'curso': cursos
        }
  return render(request,'listado_cursos.html', contexto)
@login_required
def eliminarcurso(request, id):
    devices = Curso.objects.get(id = id)
    devices.delete()
    return redirect('listado_cursos')
@login_required
def editarcurso(request,id):
    curso = Curso.objects.get(id = id)
    if request.method =='GET':
        form = CursoForm(instance = curso)
        contexto = {
            'form': form
        }
    else:
        form = CursoForm(request.POST, instance = curso)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('cursos')
    return render(request, 'cursos.html', contexto)