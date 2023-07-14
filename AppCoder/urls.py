from django.urls import path
from AppCoder import views

app_name = 'AppCoder'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    #path('cursoformulario/', views.cursoformulario, name='CursoFormulario'),
    path('profesorFormulario/', views.profesorFormulario, name='ProfesorFormulario'),
    path('estudianteFormulario/', views.estudianteFormulario, name='EstudianteFormulario'),
    path('entregableFormulario/', views.entregableFormulario, name='EntregableFormulario'),
    path('busquedaCamada', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
]
