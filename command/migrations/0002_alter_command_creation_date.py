# Generated by Django 5.1.4 on 2024-12-14 15:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
