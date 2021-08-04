"""Food app views"""

import random

from django.shortcuts import render


names = ["Mauricio", "Paco", "Jorge", "Ximena"]
food = ["Pizza", "Sushi", "Alitas", "Burritos"]


def list_food(request):
    """Return a list of food"""
    context = {
        "mi_nombre": random.choice(names),
        "food": food
    }

    return render(request, "list.html", context)


def detail_food(request, id):
    """Return a detail of food"""
    context = {
        "food": food[int(id)]
    }

    return render(request, "detail.html", context)
