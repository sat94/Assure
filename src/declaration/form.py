from compte.models import Constat
from django import forms




class DateInput(forms.DateInput):
    input_type = 'date'

class constatform(forms.ModelForm):
    class Meta:
        model=Constat
        fields = [
            "personne",
            "blesse",         
            "nom",
            "prenom",
            "age",
            "mail",
            "adresse",
            "code_postal",
            "tel",
            "voiture",
            "modeles",
            "typee",
            "couleur",
            "plaque",
            "nbpermis",
            "nbcontrat",
            "assurance",
            "circonstance",
            "nbCirconstance",
            "degatsA",
            "degatsB",
            "degatouA",
            "degatouB",
            "degatautre",
            "lieu",
            "degat_vehicule_a",
            "degat_vehicule_b",
            "commentaireA",
            "commentaireB",
            "date",
            "photo",
            "temoin",
            "signature",
            "adresse_accident"
            ]
        widgets = {
            "age": DateInput(),  
            "adresse_accident": forms.Textarea(
                attrs={
                    'rows': 2,
                    'cols': 24,
                }
            ),         
            "adresse": forms.Textarea(
                attrs={
                    'rows': 2,
                    'cols': 24,
                }
            ),  
            "circonstance" : forms.CheckboxSelectMultiple(),
            "degat_vehicule_b" :forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ),  
            "degat_vehicule_a" :forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ),  
            "date" : DateInput(), 
            "temoin":forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ), 
            "commentaireA" : forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ), 
            "commentaireB" : forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ), 
            "heure" : forms.TimeInput()
    }
                 
