from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    # name = models.CharField(max_length=50, unique=True, null=False)

    # def __str__(self):
    #     return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    image = CloudinaryField(
        "image_recipe", null=False, folder="CulinaryHub/", default=""
    )
    created_at = models.DateTimeField(default=timezone.now, null=False)
    tag_field = models.CharField(max_length=100, null=False, default="recipe")
    confirmation = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="recipes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.tag_field:
            current_tags = set(self.tags.values_list("name", flat=True))
            new_tags = set(
                tag.strip().lower() for tag in self.tag_field.split(",") if tag.strip()
            )

            # Remove tags that are no longer in tag_field
            tags_to_remove = current_tags - new_tags
            for tag_name in tags_to_remove:
                tag = Tag.objects.get(name=tag_name)
                self.tags.remove(tag)

            # Add new tags
            for tag_name in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                self.tags.add(tag)

    def get_tags(self):
        return ", ".join(tag.name for tag in self.tags.all())

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     tags = self.tag_field.split(",")
    #     for tag_name in tags:
    #         tag_name = tag_name.strip()
    #         tag, _ = Tag.objects.get_or_create(name=tag_name)
    #         self.tags.add(tag)


class Rating(models.Model):
    value = models.IntegerField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return str(self.value)
