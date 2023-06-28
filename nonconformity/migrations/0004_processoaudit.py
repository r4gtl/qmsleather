# Generated by Django 4.2.1 on 2023-06-28 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nonconformity', '0003_rapportoaudit_processo_rapportonc_fk_rapportoaudit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonconformity.rapportoaudit')),
                ('fk_processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonconformity.processo')),
            ],
        ),
    ]
