# Generated by Django 4.2.1 on 2024-02-29 16:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ricette.models


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0015_alter_dettaglioprocedura_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chem_man', '0023_alter_prodottochimico_options'),
        ('ricette', '0009_dettaglioricettarifinizione_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ricettabagnato',
            name='data_revisione',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='ricettabagnato',
            name='numero_revisione',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ricettafondo',
            name='data_revisione',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='ricettafondo',
            name='fk_articolo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ricette_fondo', to='articoli.articolo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ricettafondo',
            name='numero_revisione',
            field=models.IntegerField(blank=True, null=True),
        ),
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
        migrations.CreateModel(
            name='DettaglioRicettaBagnato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_riga', models.IntegerField()),
                ('temperatura', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=8)),
                ('tempo', models.CharField(blank=True, max_length=50, null=True)),
                ('procedura', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dettaglio_ricette_bagnato', to=settings.AUTH_USER_MODEL)),
                ('fk_operazione_ricette', models.ForeignKey(limit_choices_to=ricette.models.DettaglioRicettaBagnato.get_choices_operations, on_delete=django.db.models.deletion.CASCADE, related_name='dettaglio_ricette_bagnato', to='ricette.operazionericette')),
                ('fk_prodotto_chimico', models.ForeignKey(limit_choices_to=ricette.models.DettaglioRicettaBagnato.get_choices_chemical, on_delete=django.db.models.deletion.CASCADE, related_name='dettaglio_ricette_bagnato', to='chem_man.prodottochimico')),
                ('fk_ricetta_bagnato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dettaglio_ricette_bagnato', to='ricette.ricettabagnato')),
            ],
            options={
                'ordering': ['numero_riga'],
            },
        ),
    ]
