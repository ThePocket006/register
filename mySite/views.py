from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from formtools.wizard.views import SessionWizardView

from mySite.forms import LoginForm, EtudiantForm, EtudiantEvaluationFrom
from mySite.models import Etudiant

import hashlib
import json
import pprint


def index(request):
    return render(request, 'mySite/index.html', {'title': "Home"})

def login(request):
    if request.POST == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            student = Etudiant.objects.get(email=login, pwd=password)
            return redirect('');
        
    else:
        form = LoginForm()

    return render(request, 'mySite/students/login.html', {'form':form})


def register(request):
    if request.POST == 'POST':
        form = EtudiantForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.mdp = hashlib.sha1(student.mdp).hexdigest()
            student.save()
            return redirect('login')
    else:
        form = EtudiantForm()

    return render(request, 'mySite/students/register.html', {'form': form, 'title': "Enregistrement des étudiants"})


def choiceBranch(request):
    if request.POST == 'POST':
        form = EtudiantEvaluationFrom(request.POST)

        if form.is_valid():
            student = {}
            student.evaluation = form.save(commit=False)
            # student.save()
            return redirect('login')
    else:
        form = EtudiantEvaluationFrom()

    return render(request, 'mySite/students/choiceBranch.html', {'form': form})
