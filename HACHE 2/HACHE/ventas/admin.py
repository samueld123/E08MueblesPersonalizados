from ventas.models import  ventas
from django.contrib import admin

# Register your models here.
class VentasAdmin(admin.ModelAdmin):
    list_display = ('Sell', 'city')

admin.site.register(ventas, VentasAdmin)