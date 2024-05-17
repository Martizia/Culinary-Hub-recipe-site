from django.shortcuts import render

from recipes.forms import RecipeForm


# Create your views here.
def main(request):
    return render(request, 'recipes/index.html')


def recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'recipes/recipe.html')
    return render(request, 'recipes/recipe.html')
