# Generated by Django 4.2.16 on 2024-10-01 12:15

import core.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_itenscompra"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Usuários"},
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", core.models.user.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="passage_id",
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
