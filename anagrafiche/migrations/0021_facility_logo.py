# Generated by Django 4.2.1 on 2023-11-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anagrafiche", "0020_fornitore_e_mail"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="logo",
            field=models.ImageField(default="avatar.png", upload_to="logo"),
        ),
    ]
