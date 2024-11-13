import json
import time
import urllib.request
import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Recipe
from .forms import AddRecipe

def addRecipe(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)

        if form.is_valid():
            newRecipe = Recipe(title = form.cleaned_data['title'],
                               ingredients = form.cleaned_data['ingredients'],
                               instructions = form.cleaned_data['instructions'],
                               prepMinutes = form.cleaned_data['prepMinutes'],
                               cookMinutes = form.cleaned_data['cookMinutes'],
                               servings = form.cleaned_data['servings']
                               )
            newRecipe.save()

            # format = getIngredients(newRecipe)
            return HttpResponseRedirect("/viewRecipe/1")
        else:
            pass # TODO - Show error

    else:
        form = AddRecipe()

        form.fields['ingredients'].initial = "Separate by line breaks.  On each line:\nQuantity, Unit, Ingredient"

        return render(request, "addRecipe.html", {
            "form": form
        })

def viewRecipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    formattedIngredients = recipe.getIngredients()

    return render(request, "viewRecipe.html", {
        "recipe": recipe,
        "formattedIngredients": formattedIngredients
    })

