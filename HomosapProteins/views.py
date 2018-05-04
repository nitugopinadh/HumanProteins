from django.shortcuts import render
from django.http import HttpResponse
from HomosapProteins.models import Protein


def index(request):
    return HttpResponse("Hello, world. You're at the Protein index.")
