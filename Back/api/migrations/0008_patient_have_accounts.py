# Generated by Django 5.1.2 on 2024-12-31 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_ordonnance_medcin'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='have_accounts',
            field=models.BooleanField(default=False, null=True),
        ),
    ]