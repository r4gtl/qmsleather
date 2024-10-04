# Generated by Django 4.2.1 on 2024-10-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0029_alter_registroorelavoro_entry_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroorelavoro',
            name='entry_month',
            field=models.IntegerField(choices=[(1, 'Gennaio'), (2, 'Febbraio'), (3, 'Marzo'), (4, 'Aprile'), (5, 'Maggio'), (6, 'Giugno'), (7, 'Luglio'), (8, 'Agosto'), (9, 'Settembre'), (10, 'Ottobre'), (11, 'Novembre'), (12, 'Dicembre')], default=10),
        ),
    ]
