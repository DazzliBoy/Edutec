from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno

def index(request):
    return render(request, 'alumnos/index.html')

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        curso = request.POST['curso']
        nota = int(request.POST['nota'])

        Alumno.objects.create(nombre=nombre, apellidos=apellidos, curso=curso, nota=nota)
        return redirect('lista_alumnos')

    return render(request, 'alumnos/agregar_alumno.html')

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.nombre = request.POST['nombre']
        alumno.apellidos = request.POST['apellidos']
        alumno.curso = request.POST['curso']
        alumno.nota = int(request.POST['nota'])
        alumno.save()
        return redirect('lista_alumnos')

    return render(request, 'alumnos/editar_alumno.html', {'alumno': alumno})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()
    return redirect('lista_alumnos')
