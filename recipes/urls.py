# flake8: noqa
from django.urls import path
from recipes.views import home, sobre


urlpatterns = [
    path('', home), #Home
    path('sobre/', sobre, ) #Sobre
]
