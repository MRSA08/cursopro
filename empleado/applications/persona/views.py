from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#import models 
from .models import Empleado
#import de forms
from .forms import EmpleadoForm

#clases de ListView
#1  ¥ Listar todos los empleados de la empresa 
#2  ¥ listar empleados que pertenezcan a un area de la empresa
#3  ¥ listar empleados por trabajo
#4  ¥ listar los empleados por palabra clave
#5  ¥ listar habilidades de un empleado

class IncioView(TemplateView):
    """ vista solo de la pagina de inicio"""
    template_name = ("inicio.html")

class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by = 3
    ordering = 'first_name'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        print('===============', palabra_clave)
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        ) 
        #print('lista: ', lista)
        return lista

class ListEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class ListByAreaEmpleado(ListView):
    """ numero 2 """
    template_name="persona/list_by_area.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista
    
class ListByTrabajoEmpleado(ListView):
    """ numero 3 """
    template_name="persona/list_by_job.html"
    queryset = Empleado.objects.filter(
        job='ADMINISTRADOR'
    )

class ListEmpleadosByKword(ListView):
    """ numero 4 """
    template_name = "persona/by_kword.html"
    context_object_name= 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        print('===============', palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        ) 
        print('lista: ', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kwordh",'')
        print(type(palabra_clave))
        empleado = Empleado.objects.get(id=palabra_clave)
        return empleado.Habilidades.all()

#clases de DetailView
class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado
    #context_object_name = 'emple'
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = "Empleado del mes"
        return context
    
#templateview

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class SuccessUpdtView(TemplateView):
    template_name = "persona/successupdt.html"

#Clases de CreateView
    
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    #fields = ['first_name','second_name','job']
    # fields = [
    #     'first_name',
    #     'second_name',
    #     'job',
    #     'departamento',
    #     'Habilidades',
    #     'avatar'
    # ]
    form_class = EmpleadoForm
    success_url =  reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self,form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.second_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

#Clases para UpdateView


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html" 
    #fields = ('__all__') #tambien sirve para buscar todos los fields o parametros de la bd
    fields = [
        'first_name',
        'second_name',
        'job',
        'departamento',
        'Habilidades',
    ]
    success_url =  reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        #logica del proceso
        return super(EmpleadoUpdateView, self).form_valid(form)


#Clase DeleteView

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url =  reverse_lazy('persona_app:empleados_admin')