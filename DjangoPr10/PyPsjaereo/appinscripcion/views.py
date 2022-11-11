
"""
Importaciones 
"""
from datetime import datetime
from multiprocessing.dummy.connection import Client
from django.http import HttpResponse 
from django.template import loader
from .models import ClientePasaje
from django.urls import reverse 
from django.shortcuts import HttpResponseRedirect 

"""
Funcion home, tiene la finalidad de conectar a la plantilla 
inscripcionpasaje con el proyecto
"""
def home(request):
  template = loader.get_template('inscripcionpasaje.html') 
  client = ClientePasaje.objects.all().values()
  context = { 
      'client':client,
  }
  return HttpResponse(template.render(context,request))
"""
Funcion confirmarinscripcionpasaje, tiene la función de pasar los datos ingresados a la base de datos e 
imprimirlo dentro de la plantilla confirmarinscripcionpasaje
"""
def confirmacioninscripcionpasaje(request):
  x = request.POST['nombre'] 
  y = request.POST['direccion'] 
  z = request.POST['correo'] 
  a = request.POST['contraseña'] 
  b = request.POST['Mes'] 
  c = request.POST['Dia'] 
  d = request.POST['año'] 
  e = request.POST['gender'] 
  f = request.POST['aficiones'] 
  g = request.POST.getlist('inter[]')
  if (int(datetime.now().date().strftime("%Y"))-int(d)>=18):
    member = ClientePasaje(Nombre=x, Correo_Electronico=z, Dirección=y, Contraseña=a, 
    FechaNac= c+"/"+b+"/"+d, Sexo=e, Aficiones=f, Intereces=g, Precio=1000)  
    member.save()  
  elif (int(datetime.now().date().strftime("%Y"))-int(d)<18 and int(datetime.now().date().strftime("%Y"))-int(d)>2):
    member = ClientePasaje(Nombre=x, Correo_Electronico=z, Dirección=y, Contraseña=a, 
    FechaNac= c+"/"+b+"/"+d, Sexo=e, Aficiones=f, Intereces=g, Precio=750)  
    member.save() 
  elif (int(datetime.now().date().strftime("%Y"))-int(d)<=2):
    member = ClientePasaje(Nombre=x, Correo_Electronico=z, Dirección=y, Contraseña=a, 
    FechaNac= c+"/"+b+"/"+d, Sexo=e, Aficiones=f, Intereces=g, Precio=0)  
    member.save() 
  misclientes = ClientePasaje.objects.get(id=member.id) 
  template = loader.get_template('confirmacioninscripcionpasaje.html') 
  context = {
    'misclientes': misclientes,
  } 
  return HttpResponse(template.render(context, request)) 


  
