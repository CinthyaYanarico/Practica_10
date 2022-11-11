"""
Importaciones de modelos
"""
from django.db import models 
"""
Campos que se realizará para la tabla de la base de datos del SQlite
"""
class ClientePasaje (models.Model): 
  Nombre = models.CharField(max_length=50) 
  Dirección = models.CharField(max_length=50) 
  Correo_Electronico = models.CharField(max_length=50) 
  Contraseña = models.CharField(max_length=50) 
  FechaNac = models.CharField(max_length=50) 
  Dirección = models.CharField(max_length=50) 
  Sexo = models.CharField(max_length=50) 
  Intereces = models.CharField(max_length=50) 
  Aficiones = models.CharField(max_length=50) 
  Precio = models.IntegerField() 

  