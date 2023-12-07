from rest_framework import serializers
from .models import *


class UploadPDFForm(serializers.ModelSerializer):
    class Meta:
        model = Pdffiles
        fields = "__all__"

