from rest_framework import viewsets
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from HomosapProteins.models import Protein
from .serializers import ProteinSerializer

# ------------------------BrowserView Section---------------------------#


def index(request):
    # url:http://127.0.0.1:8000/HomosapProteins/
    return HttpResponse("Hello, world. You're at the Protein index.")

# ------------------------API Section---------------------------#


class ProteinViewSet(viewsets.ModelViewSet):
    # link: http://127.0.0.1:8000/api
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer

# ------------------------API Class based view Section---------------------------#


class ProteinList(APIView):
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
