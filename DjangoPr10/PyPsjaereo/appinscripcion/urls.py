"""
Importaciones
"""
from django.urls import path
from appinscripcion import views

"""
Rutas de la applicacion de inscripcion
"""
urlpatterns = [
    path ("",views.home,name="home"),
    path("confirmacioninscripcionpasaje/", views.confirmacioninscripcionpasaje, name='confirmacioninscripcionpasaje'),
]