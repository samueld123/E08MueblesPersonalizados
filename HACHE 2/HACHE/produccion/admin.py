from produccion.models import  produccion
from django.contrib import admin

# Register your models here.
class ProduccionAdmin(admin.ModelAdmin):
    
    list_filter = ('Begin','End')
    list_display = ('Begin','End','Advance')

admin.site.register(produccion, ProduccionAdmin)