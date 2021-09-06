from django.contrib import admin
from django.urls import path 

from . import views 

app_name = 'persona_app'

urlpatterns = [
    path(
        '', 
        views.IncioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'  
    ),    
    path(
        'listar-by-area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'listar-empleados-admin/',
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('listar-by-job/<varjob>/', views.ListByTrabajoEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-empleado-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'  
    ),    
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name ='empleado-add'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'updt-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'success-updt/', 
        views.SuccessUpdtView.as_view(), 
        name='correctoupdt'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ),
]