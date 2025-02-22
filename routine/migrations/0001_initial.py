# Generated by Django 5.1.4 on 2025-02-06 12:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_de', models.CharField(max_length=255, null=True)),
                ('routine', models.TextField()),
                ('routine_en', models.TextField(null=True)),
                ('routine_de', models.TextField(null=True)),
                ('example', models.CharField(blank=True, max_length=2000, null=True)),
                ('tooltip', models.CharField(blank=True, max_length=1000, null=True)),
                ('tooltip_en', models.CharField(blank=True, max_length=1000, null=True)),
                ('tooltip_de', models.CharField(blank=True, max_length=1000, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator_name', models.CharField(blank=True, max_length=255, null=True)),
                ('creator_email', models.CharField(blank=True, max_length=255, null=True)),
                ('creator_message', models.CharField(blank=True, max_length=10000, null=True)),
                ('copy_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routine', to='category.category')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='routine', to='category.subcategory')),
            ],
        ),
    ]
