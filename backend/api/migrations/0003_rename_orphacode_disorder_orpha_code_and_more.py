# Generated by Django 4.0.3 on 2022-03-23 00:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_disorder_hpo_delete_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disorder',
            old_name='orphaCode',
            new_name='orpha_code',
        ),
        migrations.RemoveField(
            model_name='disorder',
            name='disorderGroup',
        ),
        migrations.RemoveField(
            model_name='disorder',
            name='disorderType',
        ),
        migrations.AddField(
            model_name='disorder',
            name='symptoms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), blank=True, default=list, size=None),
        ),
        migrations.DeleteModel(
            name='HPO',
        ),
    ]
