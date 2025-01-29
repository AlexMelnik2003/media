from rest_framework import generics
from .models import FileUpload
from .serializers import FileUploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class FileUploadView(generics.ListCreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)  # Для загрузки файлов
