from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField

# Create your models here.

class materiales(models.Model):

    name= models.CharField(max_length=200, null=False, verbose_name="Nombre")
    price = models.FloatField(max_length=200, null=False, verbose_name="Precio unitario")
    

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        
                
    def __str__(self):
        return self.name