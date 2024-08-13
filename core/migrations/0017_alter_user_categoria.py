# Generated by Django 5.0.6 on 2024-08-13 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_remove_user_favorito_user_favorito"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="autores",
                to="core.categoria",
            ),
        ),
    ]