from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from HomosapProteins.models import Protein
from .serializers import ProteinSerializer

# ------------------------BrowserView Section---------------------------#


def index(request):
    return HttpResponse("Hello, world. You're at the Protein index.")

# ------------------------API Section---------------------------#


class ProteinViewSet(viewsets.ModelViewSet):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer
