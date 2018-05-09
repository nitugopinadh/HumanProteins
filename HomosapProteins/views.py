from rest_framework import viewsets
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from HomosapProteins.models import Protein
from .serializers import ProteinSerializer
import logging
logger = logging.getLogger(__name__)
# ------------------------BrowserView Section---------------------------#


def index(request):
    # url:http://127.0.0.1:8000/HomosapProteins/
    # logger.error("this is a debug message!")
    # a = {1: 'nitu', 2: 'neha'}
    # myerrorlog(a)
    return HttpResponse("Hello, world. You're at the Protein index.")

# ------------------------API Section---------------------------#


class ProteinViewSet(viewsets.ModelViewSet):
    # link: http://127.0.0.1:8000/api
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer


class ProteinList(APIView):
    # API Class based view Section
    def get(self, request):
        # link: http://127.0.0.1:8000/api/protein/?p_id=1433E_HUMAN
        protein_id = request.GET['p_id']
        # protein = Protein.objects.get(p_id='1433B_HUMAN')
        # protein = Protein.objects.get(p_id=protein_id)
        # serializer = ProteinSerializer(protein, many=False)

        protein = Protein.objects.filter(p_id=protein_id)
        serializer = ProteinSerializer(protein, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#------------------------------Log file section-----------------------------------------------#


def myerrorlog(text):
    # Debug file location: /error.log
    # logger.error("this is a debug message!")
    logger.error("**********************")
    logger.error(text)
    logger.error("**********************")
