# Generated by Django 4.2.1 on 2023-07-20 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chem_man', '0011_alter_dettaglioordineprodottochimico_fk_prodotto_chimico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dettaglioordineprodottochimico',
            name='fk_prodotto_chimico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chem_man.prodottochimico'),
        ),
    ]
