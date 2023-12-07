from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import *
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.generics import *
# Create your views here.
from extraction_app.extraction import extract_text
import time
import concurrent.futures
import os


def index(request):
    return HttpResponse("hello world")


class TextExtractionAPI(CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = UploadPDFForm

    def post(self, request, *args, **kwargs):
        try:
            files = request.FILES.getlist('pdf')
            serialized_files = []

            with concurrent.futures.ThreadPoolExecutor() as executor:
                for file in files:
                    data = {'pdf': file}
                    serializer = UploadPDFForm(data=data)
                    if serializer.is_valid():
                        saved_instance = serializer.save()
                        serialized_files.append({
                            'pdf': saved_instance.pdf.path,
                            'id': saved_instance.id
                        })
                        # Submit each file for processing in a separate thread
                        executor.submit(extract_text, saved_instance.pdf.path, saved_instance.id)

                data = {
                    'Response Code': status.HTTP_201_CREATED,
                    'Status': 'TRUE',
                    'Message': 'Data Uploaded and Text file is created',
                    "Error": 'None',
                    'Data': serialized_files,
                }
                return Response(data)

        except Exception as e:
            data = {
                'Response Code': status.HTTP_400_BAD_REQUEST,
                'Status': 'FALSE',
                'Message': 'Upload Failed',
                "Error": str(e),
                'Data': [],
            }
            return Response(data)
