from django.db import models
from django.core.files.base import ContentFile
import os


class Pdffiles(models.Model):
    pdf = models.FileField()
