# Generated by Django 4.2.1 on 2024-12-14 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafiche', '0038_alter_xrdocumentitrasportatore_fornitore_rifiuti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xrdocumentitrasportatore',
            name='fornitore_rifiuti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documenti_trasportatore', to='anagrafiche.fornitorerifiuti'),
        ),
    ]
