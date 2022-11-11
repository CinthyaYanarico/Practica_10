"""
Importaciones 
"""
from django.contrib import admin
from django.urls import include,path
"""
Ruta importantes para conectar con la aplicación y el administrador 
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path ("",include("appinscripcion.urls")),
]
