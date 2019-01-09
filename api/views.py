import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from mySite.models import Filiere, Niveau

# Create your views here.


def index(request):
    data = {
        'status': 200,
        'error': '',
        'msg': '',
        'data': {},
    }
    return JsonResponse(data)


def get_filiere(request):
    filieres = [item for item in Filiere.objects.values('id', 'libelle')]
    data = {
        'status': 200,
        'error': '',
        'msg': '',
        'data': {
            'filiere': filieres
        },
    }
    
    return JsonResponse(data)


def get_niveau(request):
    niveaux = [item for item in Niveau.objects.values('id', 'libelle')]
    data = {
        'status': 200,
        'error': '',
        'msg': '',
        'data': {
            'niveau': niveaux
        },
    }

    return JsonResponse(data)
