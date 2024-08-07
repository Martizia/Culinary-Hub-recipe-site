from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from recipes.forms import RecipeForm
from recipes.models import Recipe


# Create your views here.
def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


@login_required
def recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            tag_length = len(form.cleaned_data['tag_field'].split(','))
            if tag_length > 7:
                form.add_error('tag_field', 'Too many tags')
                return render(request, 'recipes/recipe.html', {'form': form})
            form.save()
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect('recipes:main')
        else:
            return render(request, 'recipes/recipe.html', {'form': form})

    return render(request, 'recipes/recipe.html', {'form': RecipeForm()})


def detail(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe_page})


@login_required
def delete(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    recipe_page.delete()
    return redirect('recipes:main')



