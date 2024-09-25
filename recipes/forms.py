from django.forms import CharField, ModelForm
from .models import Recipe
from cloudinary.forms import CloudinaryFileField


class RecipeForm(ModelForm):
    title = CharField(label="Title", required=True)
    description = CharField(label="Description", required=True)
    tag_field = CharField(label="Tags", required=False)
    image = CloudinaryFileField(
        options={
            "folder": "CulinaryHub/",
            "use_filename": True,
            "unique_filename": False,
            "overwrite": True,
            "crop": "limit",
            "width": 300,
            "height": 300,
            "eager": [{"width": 300, "height": 300, "crop": "fill"}],
        }
    )

    class Meta:
        model = Recipe
        fields = ["title", "description", "tag_field", "image"]
