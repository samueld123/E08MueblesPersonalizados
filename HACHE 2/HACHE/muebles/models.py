from django.db import models
from tkinter import *
from django.db.models.fields import AutoField
from django.forms import fields
from django.forms.fields import ChoiceField
from proveedor.models import proveedor
from produccion.models import produccion
# Create your models here.

class muebles(models.Model):

    
    name= models.CharField(max_length=200, null=False, verbose_name="Nombre")
    price = models.FloatField(max_length=200, null=False, verbose_name="Precio")
    lenght = models.FloatField(max_length=200, null=False, verbose_name="Largo")
    width = models.FloatField(max_length=200, null=False, verbose_name="Ancho")
    height = models.FloatField(max_length=200, null=False, verbose_name="Alto")
    status = models.CharField(max_length=200, null=False, verbose_name="Estado", choices= (
        ('Nuevo', 'Nuevo'),
        ('En producción', 'En producción'),
        ('Entregado', 'Entregado'),
    ))
    proveedor = models.ForeignKey(proveedor, null= True, blank= True, on_delete=models.CASCADE ) 
    produccion = models.ForeignKey(produccion, null= True, blank= True, on_delete=models.CASCADE )
    
    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"
        
                
    def __str__(self):
        return self.name
