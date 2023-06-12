# Generated by Django 4.2.1 on 2023-06-12 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manualeprocedure", "0003_revisioneprocedura_revisionemodulo_modulo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revisionemodulo",
            name="documento",
            field=models.FileField(
                blank=True, null=True, upload_to="procedure/moduli/"
            ),
        ),
        migrations.AlterField(
            model_name="revisionemodulo",
            name="fk_modulo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="manualeprocedure.modulo",
            ),
        ),
    ]
