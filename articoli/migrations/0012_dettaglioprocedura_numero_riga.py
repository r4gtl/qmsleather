# Generated by Django 4.2.1 on 2023-10-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articoli", "0011_alter_procedura_nr_procedura_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dettaglioprocedura",
            name="numero_riga",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
