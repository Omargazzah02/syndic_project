from django.db import models
from django.core.validators import FileExtensionValidator


class Document (models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='Autre')
    pdf_file = models.FileField(upload_to='pdfs/',  validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


