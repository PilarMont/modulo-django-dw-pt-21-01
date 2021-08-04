"""Bank URL Configuration"""

from django.urls import path

from food.views import list_food, detail_food

urlpatterns = [
    path('', list_food),
    path('<int:id>', detail_food),
]
