# Generated by Django 5.1.2 on 2025-01-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_medcalrecord_unite_alter_medcalrecord_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilanbiologique',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bilanradiologique',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='', max_length=100),
        ),
    ]