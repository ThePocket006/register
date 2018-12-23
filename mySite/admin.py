from django.contrib import admin

from .models import Etudiant, Ue, Semestre, SujetEvaluation, Filiere, Periode, Niveau

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

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Ue)
admin.site.register(Semestre)
admin.site.register(SujetEvaluation)
admin.site.register(Filiere)
admin.site.register(Periode)
admin.site.register(Niveau)