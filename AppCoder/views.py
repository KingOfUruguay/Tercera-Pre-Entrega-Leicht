from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def curso(request):
    curso = Curso(nombre='Desarollo Web', camada='19881')
    curso.save()

    documentodetexto = f'---->Curso: {curso.nombre} Camdada: {curso.camada}'

    return HttpResponse(documentodetexto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            curso = Curso(nombre=info['nombre'], 
                          camada=info['camada'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, 'AppCoder/cursos.html', {'miFormulario': miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            profesor = Profesor(nombre=info['nombre'], 
                                apellido=info['apellido'],
                                email=info['email'],
                                profesion=info['profesion'])
            profesor.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})

def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=info['nombre'], 
                                    apellido=info['apellido'],
                                    email=info['email'])
            estudiante.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EstudianteFormulario()

    return render(request, 'AppCoder/estudianteFormulario.html', {'miFormulario': miFormulario})

def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            entregable = Entregable(nombre=info['nombre'], 
                                    fecha_entrega=info['fecha_entrega'],
                                    entregado=info['entregado'])
            entregable.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EntregableFormulario()

    return render(request, 'AppCoder/entregableFormulario.html', {'miFormulario': miFormulario})

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'AppCoder/inicio.html', {'cursos':curso, 'camada':camada})
    
    else:
        respuesta = 'No enviaste datos.'
    

    return HttpResponse(respuesta)
