from cliente.models import  clientes
from django.contrib import admin

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name','docu', 'number_docu', 'email', 'phone', 'address')

admin.site.register(clientes, ClienteAdmin)