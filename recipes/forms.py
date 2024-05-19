from django.forms import CharField, ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    title = CharField(label='Title', required=True)
    description = CharField(label='Description', required=True)
    tag_field = CharField(label='Tags', required=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'tag_field']
