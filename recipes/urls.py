from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.main, name='main'),
    path('recipes/', views.recipe, name='recipe'),
    path('recipes/<int:recipe_id>/', views.detail, name='detail'),
    path('recipes/delete/<int:recipe_id>/', views.delete, name='delete'),
]