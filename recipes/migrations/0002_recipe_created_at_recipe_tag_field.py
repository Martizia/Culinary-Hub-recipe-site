# Generated by Django 5.0.6 on 2024-05-14 15:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tag_field',
            field=models.CharField(default='recipe', max_length=100),
        ),
    ]