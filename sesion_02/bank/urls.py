"""Bank URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path('food/', include('food.urls')),
]
