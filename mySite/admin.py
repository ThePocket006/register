from django.contrib import admin

from .models import Etudiant, Ue, Semestre, Evaluation, Filiere, Periode, Niveau, EtudiantEvaluation, FiliereNiveau, TypeEvaluation, UeFiliereNiveau

class FiliereInline(admin.TabularInline):
    model = Filiere
    extra = 1

class EtudiantAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['matricule']}),
    #     ('Date naissance', {'fields': ['date'], 'classes': ['collapse']}),
    # ]
    list_display = ('matricule', 'nom', 'prenom', 'date')
    # list_filter = ['pub_date']
    search_fields = ['matricule', 'nom', 'prenom']

class SemestreAdmin(admin.ModelAdmin):
    list_display = ('abr', 'libelle')
    search_fields = ['libelle', 'abr']

class TypeEvaluationAdmin(admin.ModelAdmin):
    list_display = ('abr', 'libelle')
    search_fields = ['libelle', 'abr']

class NiveauAdmin(admin.ModelAdmin):
    list_display = ('abr', 'libelle')
    search_fields = ['libelle', 'abr']


class UeAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom')
    search_fields = ['nom', 'code']
    

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Ue, UeAdmin)
admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Evaluation)
admin.site.register(Filiere)
admin.site.register(Periode)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(EtudiantEvaluation)
admin.site.register(FiliereNiveau)
admin.site.register(TypeEvaluation, TypeEvaluationAdmin)
admin.site.register(UeFiliereNiveau)
