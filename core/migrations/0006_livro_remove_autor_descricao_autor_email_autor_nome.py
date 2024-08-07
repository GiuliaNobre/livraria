# Generated by Django 5.0.2 on 2024-07-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_autor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="autor",
            name="descricao",
        ),
        migrations.AddField(
            model_name="autor",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="autor",
            name="nome",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
