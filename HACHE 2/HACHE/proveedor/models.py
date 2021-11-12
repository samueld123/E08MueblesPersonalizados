from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField

# Create your models here.

class proveedor(models.Model):

    name= models.CharField(max_length=200, null=False, verbose_name="Nombre")
    docu = models.CharField(max_length=200, null=False, verbose_name="Tipo de documento", choices= (
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extrangería'),
        ('TI', 'Tarjeta de identidad'),
        ('NTI', 'NIT'),
        ('PAS', 'Pasaporte'),
    ))
    number_docu= models.CharField(max_length=200, null=False, verbose_name="Número de documento")
    email= models.CharField(max_length=200, null=False, verbose_name="Correo electónico")
    phone= models.CharField(max_length=200, null=False, verbose_name="Telefono")
    special= models.CharField(max_length=200, null=False, verbose_name="Especialidad")
    

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        
                
    def __str__(self):
        return self.name