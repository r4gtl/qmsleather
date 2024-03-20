# Generated by Django 4.2.1 on 2024-03-20 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articoli', '0018_caratteristicaprocedura_numero_riga'),
        ('ricette', '0010_ricettabagnato_data_revisione_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ricettacolorebagnato',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ricettacolorebagnato', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ricettacolorebagnato',
            name='fk_articolo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricettacolorebagnato', to='articoli.articolo'),
        ),
        migrations.AlterField(
            model_name='ricettacolorebagnato',
            name='fk_colore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricettacolorebagnato', to='articoli.colore'),
        ),
        migrations.AlterField(
            model_name='ricettacolorebagnato',
            name='fk_ricetta_bagnato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ricettacolorebagnato', to='ricette.ricettabagnato'),
        ),
    ]
