"""Bank URL Configuration"""

from django.urls import path

from calculadora.views import hola_django, perfil, suma

urlpatterns = [
    path("hola-django", hola_django),
    path("perfil/<str:username>", perfil),
    path("suma/<int:num1>/<int:num2>", suma),
]
