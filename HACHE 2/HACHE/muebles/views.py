from django.shortcuts import render, HttpResponse, redirect
from .models import muebles
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Muebles(request):
    mueble = muebles.objects.all() 
    print(mueble)
    return render(request, "muebles/tables.html", {'muebles': mueble})
    
@xframe_options_exempt
def Calendario(request):
    return render(request, "muebles/calendario.html")