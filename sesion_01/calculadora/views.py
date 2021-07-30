"""Calculadora views"""

from django.http import HttpResponse, JsonResponse


def hola_django(request):
    """Saluda al usuario"""
    if "name" in request.GET:
        name = request.GET["name"]
    else:
        name = "Django"

    message = "Hola {}".format(name)
    return HttpResponse(message)


def perfil(request, username):
    """Muestra el perfil del usuario"""
    message = "Hola, @{}".format(username)
    return HttpResponse(message)


def suma(request, num1, num2):
    """Suma los numeros"""
    result = num1 + num2
    result = "{} + {} = {}".format(num1, num2, result)
    message = {
        "result": result
    }
    return JsonResponse(message)
