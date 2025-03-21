# Generated by Django 5.1.6 on 2025-03-21 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pdf_file',
            field=models.FileField(upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
