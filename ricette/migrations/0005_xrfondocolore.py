# Generated by Django 4.2.1 on 2024-03-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0018_caratteristicaprocedura_numero_riga'),
        ('ricette', '0004_dettaglioricettacolorebagnato_procedura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='XRFondoColore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ricetta', models.IntegerField(default=None)),
                ('fk_colore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_fondo_colore', to='articoli.colore')),
            ],
        ),
    ]
