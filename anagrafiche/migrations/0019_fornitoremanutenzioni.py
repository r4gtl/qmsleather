# Generated by Django 4.2.1 on 2023-08-04 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("anagrafiche", "0018_fornitorerifiuti_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FornitoreManutenzioni",
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
                (
                    "fornitore_ptr",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        related_name="fornitore_ptr_manutenzioni",
                        to="anagrafiche.fornitore",
                    ),
                ),
                ("prova", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
