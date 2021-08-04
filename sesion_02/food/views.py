"""Food app views"""

from django.shortcuts import render, redirect


food = []


def list_food(request):
    """Return a list of food"""
    context = {
        "food": food
    }

    return render(request, "list.html", context)


def detail_food(request, id):
    """Return a detail of food"""
    context = {
        "food": food[int(id)]
    }

    return render(request, "detail.html", context)


def create_food(request):
    """Create a food"""
    if request.method == 'POST':
        name = request.POST['name']
        food.append(name)
        return redirect('food:list')

    return render(request, "create.html")
