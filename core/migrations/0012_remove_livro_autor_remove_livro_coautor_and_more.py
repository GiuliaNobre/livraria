# Generated by Django 5.0.2 on 2024-08-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_livro_coautor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="autor",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="coautor",
        ),
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]