from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField

# Create your models here.

class ventas(models.Model):

    Sell= models.DateField(max_length=200, null=False, verbose_name="Fecha venta")
    city = models.CharField(max_length=200, null=False, verbose_name="Ciudad")
    
    

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
                
    def __str__(self):
        return self.name