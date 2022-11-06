# Generated by Django 4.1.3 on 2022-11-06 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PartieAdmin', '0003_alter_enseignant_chefdepartement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='chefdepartement',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='chefdepartement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chefdepartement', to='PartieAdmin.departement'),
        ),
    ]