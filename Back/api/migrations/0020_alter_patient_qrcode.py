# Generated by Django 5.0.4 on 2025-01-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_patient_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='qrcode',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]