# flake8: noqa
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
# Create your views here.

def home(request):    
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    
    if not recipes:
        raise Http404('Not found 🥲')
    
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'name': 'Receitas',
        'recipes': recipes,
    })
    

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html', context= {
        'name': 'Receitas',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
