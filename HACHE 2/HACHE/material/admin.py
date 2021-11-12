from material.models import  materiales
from django.contrib import admin

# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name','price')

admin.site.register(materiales, MaterialAdmin)