# Generated by Django 5.0.7 on 2024-09-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
