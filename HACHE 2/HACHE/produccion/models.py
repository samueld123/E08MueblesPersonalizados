from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField
# from muebles.models import muebles
from material.models import materiales

# Create your models here.

class produccion(models.Model):

    Begin= models.DateField(max_length=200, null=False, verbose_name="Fecha inicio")
    End= models.DateField(max_length=200, null=False, verbose_name="Fecha entrega")
    Advance= models.FloatField(max_length=200, null=False, verbose_name="Anticipo")
    # muebles = models.ForeignKey(muebles, null= True, blank= True, on_delete=models.CASCADE)
    materiales = models.ForeignKey(materiales, null= True, blank= True, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Producción"
        verbose_name_plural = "Producciones"
        
    