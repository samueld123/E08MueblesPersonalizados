from muebles.models import  muebles
from django.contrib import admin

# Register your models here.
class MueblesAdmin(admin.ModelAdmin):
    list_filter = ('name','status')
    list_display = ('name','price', 'lenght', 'width', 'height', 'status')

admin.site.register(muebles, MueblesAdmin)