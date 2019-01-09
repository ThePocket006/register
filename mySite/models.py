# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each OneToOneField has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

GENRE_CHOICES = (('M', 'Masculin'), ('F', 'Féminin'))

class Filiere(models.Model):
    libelle = models.TextField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

    class Meta:
        managed = True
        db_table = 'Filiere'


class Niveau(models.Model):
    libelle = models.CharField(max_length=50)
    abr = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.libelle

    class Meta:
        managed = True
        db_table = 'Niveau'


class Semestre(models.Model):
    libelle = models.CharField(max_length=50)
    abr = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle

    class Meta:
        managed = True
        db_table = 'Semestre'


class Etudiant(models.Model):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=1, choices=GENRE_CHOICES)
    datenaiss = models.DateField(db_column='dateNaiss')  # Field name made lowercase.
    lieunaiss = models.CharField(db_column='lieuNaiss', max_length=50, blank=True, null=True)   # Field name made lowercase.
    email = models.CharField(max_length=255)
    mdp = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.matricule

    class Meta:
        managed = True
        db_table = 'etudiant'


class EtudiantEvaluation(models.Model):
    etudiant = models.OneToOneField(Etudiant, models.CASCADE)
    evaluation = models.OneToOneField('Evaluation', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'etudiant_evaluation'


class EtudiantFnPeriode(models.Model):
    etudiant = models.OneToOneField(Etudiant, models.CASCADE)
    filiere_niveau = models.OneToOneField('FiliereNiveau', models.CASCADE)
    periode = models.OneToOneField('Periode', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'etudiant_filiere_niveau_periode'


class Evaluation(models.Model):
    ue_fn = models.OneToOneField('UeFiliereNiveau', models.CASCADE)
    semestre = models.OneToOneField('Semestre', models.CASCADE)
    type_evaluation = models.OneToOneField('TypeEvaluation', models.CASCADE)
    session = models.OneToOneField('Session', models.CASCADE, related_name='fk_Evaluation')
    periode = models.OneToOneField('Periode', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'evaluation'


class FiliereNiveau(models.Model):
    filiere = models.OneToOneField('Filiere', models.CASCADE)
    niveau = models.OneToOneField('Niveau', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'filiere_niveau'


class Periode(models.Model):
    datedebut = models.DateField(db_column='dateDebut')  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin')  # Field name made lowercase.

    def __str__(self):
        return "Du " + self.datedebut + " au " + self.datefin

    class Meta:
        managed = True
        db_table = 'periode'


class Session(models.Model):
    Evaluation = models.OneToOneField(Evaluation, models.CASCADE, related_name='fk_Session')
    debut = models.DateField()
    fin = models.DateField()

    def __str__(self):
        return "Du " + self.debut + " au " + self.fin

    class Meta:
        managed = True
        db_table = 'session'


class TypeEvaluation(models.Model):
    libelle = models.CharField(max_length=200)
    abr = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.libelle
    

    class Meta:
        managed = True
        db_table = 'type_evaluation'


class Ue(models.Model):
    nom = models.TextField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'ue'


class UeFiliereNiveau(models.Model):
    ue = models.OneToOneField(Ue, models.CASCADE)
    filiere_niveau = models.OneToOneField(FiliereNiveau, models.CASCADE)
    code = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ue_filiere_niveau'
