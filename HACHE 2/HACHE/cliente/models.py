from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField

# Create your models here.

class clientes(models.Model):

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
    address= models.CharField(max_length=200, null=False, verbose_name="Dirección")
    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
                
    def __str__(self):
        return self.name