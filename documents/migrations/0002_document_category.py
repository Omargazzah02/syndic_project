# Generated by Django 5.1.6 on 2025-03-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.CharField(default='Autre', max_length=255),
        ),
    ]
