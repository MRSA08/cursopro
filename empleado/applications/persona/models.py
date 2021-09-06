from django.db import models
from django.db.models.fields.files import ImageField

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    """Model definition for Habilidades."""
    
    habilidades = models.CharField('Habilidades', max_length=50)
    
    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidades


class Empleado(models.Model):
    """ Modelo para tabla empleado """

    JOB_CHOICES = {
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    }

    first_name = models.CharField('Nombres', max_length=60)
    second_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120,blank=True)
    job = models.CharField('Trabajo',max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', height_field=None,blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Los empleados de la empresa'
        ordering = ['first_name','second_name']
        unique_together = ('first_name','second_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.second_name