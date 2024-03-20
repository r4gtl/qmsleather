# Generated by Django 4.2.1 on 2024-03-20 15:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articoli', '0018_caratteristicaprocedura_numero_riga'),
        ('ricette', '0013_delete_ricettacolorebagnato'),
    ]

    operations = [
        migrations.CreateModel(
            name='RicettaColoreBagnato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ricetta', models.IntegerField(default=None)),
                ('data_ricetta', models.DateField(default=datetime.date.today)),
                ('numero_revisione', models.IntegerField(blank=True, null=True)),
                ('data_revisione', models.DateField(default=datetime.date.today)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ricette_colore_bagnato', to=settings.AUTH_USER_MODEL)),
                ('fk_articolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricette_colore_bagnato', to='articoli.articolo')),
                ('fk_colore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricette_colore_bagnato', to='articoli.colore')),
                ('fk_ricetta_bagnato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricette_colore_bagnato', to='ricette.ricettabagnato')),
            ],
            options={
                'ordering': ['-data_ricetta'],
            },
        ),
    ]
