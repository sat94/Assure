from compte.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
import os


def delete_previous_picture(previous,new):
    if previous != new:
        os.remove(previous)
        return True
    return False  



class DateInput(forms.DateInput):
    input_type = 'date'


        

class SignupForm(UserCreationForm):  
     class Meta:
        model = MyUser
        fields = [
            "email",
            "nom", 
            "password1",
            "password2",
            "prenom", 
            "nbpermis",
            "jeune",
            "age",
            "sexe",
            "numberPhone",             
            "adresse", 
            "postal", 
            "ville",
            "photo",
            "Contrat",            
            "marque",
            "modeles",
            "plaque",
            "annee",
            "couleur",
            "photo_voiture",
            "chevaux",
            "typee",                         
            ]
        widgets = {
            "age": DateInput(),         
            "adresse": forms.Textarea(
                attrs={
                    'rows': 2,
                    'cols': 24,
                }
            ),          
            "password" : forms.PasswordInput(),
            "annee" : DateInput()
        }

        
       
