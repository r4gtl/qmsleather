# Generated by Django 4.2.1 on 2023-07-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafiche', '0010_rename_prova_fornitoreprodottichimici_id_zdhc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornitorelavorazioniesterne',
            name='is_lwg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fornitorepelli',
            name='is_lwg',
            field=models.BooleanField(default=False),
        ),
    ]
