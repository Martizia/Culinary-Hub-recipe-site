from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.main, name="main"),
    path("recipes/", views.recipe, name="recipe"),
    path("recipes/<int:recipe_id>/", views.detail, name="detail"),
    path("recipes/delete/<int:recipe_id>/", views.delete_main, name="delete_main"),
    path(
        "recipes/delete_conf/<int:recipe_id>/",
        views.delete_conf,
        name="delete_conf",
    ),
    path(
        "recipes/recipe-confirmation/",
        views.recipe_conf,
        name="recipe_confirmation",
    ),
    path("recipes/recipe-confirmation/<int:recipe_id>/", views.confirm, name="confirm"),
    path("tag/<slug:tag_slug>/", views.recipe_list, name="tag"),
]
