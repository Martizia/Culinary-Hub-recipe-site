# Generated by Django 5.0.6 on 2024-06-12 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0005_user_delete_myuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
