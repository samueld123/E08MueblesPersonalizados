from proveedor.models import  proveedor
from django.contrib import admin

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('name','docu', 'number_docu', 'email', 'phone', 'special')

admin.site.register(proveedor, ProveedorAdmin)