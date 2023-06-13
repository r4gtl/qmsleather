# Generated by Django 4.2.1 on 2023-06-13 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("anagrafiche", "0006_alter_transfervalue_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Attrezzatura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codice_attrezzatura", models.CharField(max_length=10)),
                ("descrizione", models.CharField(max_length=50)),
                ("modello", models.CharField(max_length=100)),
                ("serie_matricola", models.CharField(max_length=50)),
                ("is_taratura", models.BooleanField(default=False)),
                ("periodo_taratura", models.CharField(max_length=50)),
                ("note", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="attrezzatura",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Taratura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_taratura", models.DateField()),
                ("is_conforme", models.BooleanField(default=True)),
                ("prossima_scadenza", models.DateField()),
                ("note", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="taratura",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "fk_attrezzatura",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manutenzioni.attrezzatura",
                    ),
                ),
            ],
            options={
                "ordering": ["-data_taratura"],
            },
        ),
        migrations.CreateModel(
            name="ManutenzioneStraordinaria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_manutenzione", models.DateField()),
                ("descrizione", models.CharField(max_length=100)),
                ("importo", models.DecimalField(decimal_places=3, max_digits=8)),
                ("ore_fermo", models.DecimalField(decimal_places=2, max_digits=6)),
                ("ft_prot", models.CharField(blank=True, max_length=20, null=True)),
                ("data_fattura", models.DateField()),
                ("note", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="manutenzione_straordinaria",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "fk_attrezzatura",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manutenzioni.attrezzatura",
                    ),
                ),
                (
                    "fk_fornitore",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="anagrafiche.fornitore",
                    ),
                ),
            ],
            options={
                "ordering": ["-data_manutenzione"],
            },
        ),
    ]
