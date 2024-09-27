from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from recipes.forms import RecipeForm
from recipes.models import Recipe, Tag


def is_staff(user):
    return user.is_authenticated and user.is_staff


def main(request):
    recipes = Recipe.objects.filter(confirmation=True)
    return render(request, "recipes/index.html", {"recipes": recipes})


@login_required
def recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            tag_length = len(form.cleaned_data["tag_field"].split(","))
            if tag_length > 7:
                form.add_error("tag_field", "Too many tags")
                return render(request, "recipes/recipe.html", {"form": form})
            form.save()
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect("recipes:main")
        else:
            return render(request, "recipes/recipe.html", {"form": form})

    return render(request, "recipes/recipe.html", {"form": RecipeForm()})


def detail(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe_page})


@login_required
def delete_main(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    recipe_page.delete()
    return redirect("recipes:main")


@login_required
def delete_conf(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    recipe_page.delete()
    return redirect("recipes:recipe_confirmation")


@user_passes_test(is_staff)
@login_required
def recipe_conf(request):
    recipes = Recipe.objects.filter(confirmation=False)
    return render(request, "recipes/recipe-conf.html", {"recipes": recipes})


@login_required
def confirm(request, recipe_id):
    recipe_page = get_object_or_404(Recipe, pk=recipe_id)
    recipe_page.confirmation = True
    recipe_page.save()
    return redirect("recipes:recipe_confirmation")


def recipe_list(request, tag_slug=None):
    recipes = Recipe.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        recipes = recipes.filter(tags=tag)

    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "tag": tag})
