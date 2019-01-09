from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from mySite.models import Etudiant, Filiere, Niveau, EtudiantEvaluation, EtudiantFnPeriode


class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=255, required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        login = cleaned_data.get('login')
        password = cleaned_data.get('password')

class EtudiantForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    mdp = forms.CharField(max_length=255, min_length=8, required=True, label='Mots de passe', widget=forms.PasswordInput())
    
    class Meta:
        model = Etudiant
        fields = ('matricule', 'nom', 'prenom', 'sexe', 'datenaiss', 'lieunaiss', 'email', 'mdp')
        widgets = {
            'datenaiss': DatePickerInput(format='%m/%d/%Y'),
        }
        labels = {
            'mdp':'Mots de passe',
            'datenaiss':'Date de naissance',
            'lieunaiss':'Lieu de naissance',
            'sexe':'Genre'
        }

class EtudiantEvaluationFrom(forms.ModelForm):
    class Meta:
        model = EtudiantEvaluation
        fields = '__all__'


class EtudiantFnPeriodeForm(forms.ModelForm):
    # filiere = forms.Select()
    class Meta:
        model = EtudiantFnPeriode
        fields = '__all__'
