from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('recipe/', views.recipe, name='recipe'),
]