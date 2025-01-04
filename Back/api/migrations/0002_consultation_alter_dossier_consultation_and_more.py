# Generated by Django 5.1.2 on 2024-12-27 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('resume', models.TextField()),
                ('medcin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medcin_sejour', to='api.medcin')),
                ('soin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soin_sejour', to='api.soin')),
            ],
        ),
        migrations.AlterField(
            model_name='dossier',
            name='consultation',
            field=models.ManyToManyField(blank=True, null=True, related_name='cons_dossier', to='api.consultation'),
        ),
        migrations.DeleteModel(
            name='Consulatation',
        ),
    ]
