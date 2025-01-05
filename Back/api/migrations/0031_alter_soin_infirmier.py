# Generated by Django 5.0.4 on 2025-01-04 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_rename_typesoin_soin_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soin',
            name='infirmier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infirmier_soin', to='api.infirmier'),
        ),
    ]