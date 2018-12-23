import datetime

from django.db import models
from django.utils import timezone

# Classe Etudiant
class Etudiant(models.Model):
    SEXE_CHOICES=(
        ('M','Masculin'),
        ('F','Féminin'),
    )
    # Les champs de la classe Etudiant
    matricule=models.CharField(max_length=8, primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50, blank=True, null=True)
    date=models.DateField()
    lieuNaiss=models.CharField(max_length=50)
    sexe=models.CharField(max_length=1, choices=SEXE_CHOICES)
    login=models.CharField(max_length=50)
    motPasse=models.CharField(max_length=50)
    # Les méthodes de la classe Etudiant

# Classe UE
class Ue(models.Model):
    codeUE=models.CharField(max_length=6, primary_key=True)
    nomUE=models.CharField(max_length=50)
    # Les méthodes de la classe UE

# Classe Semestre
class Semestre(models.Model):
    SEMESTRE_CHOICES=(
        ('S1','Semestre 1'),
        ('S2','Semestre 2'),
        ('S3','Semestre 3'),
        ('S4','Semestre 4'),
        ('S5','Semestre 5'),
        ('S6','Semestre 6'),
    )
    codeSemestre=models.IntegerField()
    nomSemestre=models.CharField(max_length=1, choices=SEMESTRE_CHOICES)
    # Les méthodes de la classe Semestre

# Classe SujetEvaluation
class SujetEvaluation(models.Model):
    nomSujet=models.CharField(max_length=50)
    session=models.IntegerField()
    date=models.DateField()
    # Les méthodes de la classe SujetEvaluation

# Classe Filiere
class Filiere(models.Model):
    FILIERE_CHOICES=(
        ('GEO','Géographe'),
        ('HIS','Histoire'),
        ('INF','Informatique'),
        ('MAT','Mathématiques'),
        ('DRT','Droit'),
        ('LIT','Littérature et Langue'),
    )
    codeFiliere=models.IntegerField()
    filiere=models.CharField(max_length=1, choices=FILIERE_CHOICES)
    # Les méthodes de la classe Filiere

# Classe Periode
class Periode(models.Model):
    dateDebut=models.DateField()
    dateFin=models.DateField()
    # Les méthodes de la classe Periode

# Classe Niveau
class Niveau(models.Model):
    libelle=models.CharField(max_length=50)
    abbreviation=models.CharField(max_length=10)
    # Les méthodes de la classe Niveau