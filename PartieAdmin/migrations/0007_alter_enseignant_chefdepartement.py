# Generated by Django 4.1.3 on 2022-11-07 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("PartieAdmin", "0006_absence_heure"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enseignant",
            name="chefdepartement",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chefdepartement",
                to="PartieAdmin.departement",
            ),
        ),
    ]
