# Generated by Django 5.0.2 on 2024-08-30 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_rename_autor_livro_autores"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
