# Generated by Django 5.1.2 on 2024-12-31 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_dossier_dateadmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='dateAdmission',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
