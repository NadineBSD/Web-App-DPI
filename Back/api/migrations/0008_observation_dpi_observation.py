# Generated by Django 5.1.4 on 2024-12-26 16:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_bilan_ordonnance_resume_consultation_soin_dpi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0.0)),
                ('tension', models.FloatField(default=0.0)),
                ('frequanceCardiaque', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='dpi',
            name='observation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.observation'),
        ),
    ]
