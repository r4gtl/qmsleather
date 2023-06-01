# Generated by Django 4.2.1 on 2023-06-01 14:01

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanresource',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='humanresource',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Maschio'), ('F', 'Femmina')], max_length=1, null=True),
        ),
    ]
