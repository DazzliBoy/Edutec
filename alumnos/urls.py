from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]
