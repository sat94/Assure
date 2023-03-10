from django.shortcuts import render, redirect, HttpResponse
from compte.models import *
from django.contrib.auth import logout
from compte.forms import *
from django.contrib.auth import get_user_model
from compte.models import Marque, Modele, Departement, Region, Ville, Remorque, Garage


def login(request):    
    return render(request, "login.html", {'navbar': 'login'})

def inscription(request): 
    context={}
    form=SignupForm 
    ville = Ville.objects.all() 
    marques = Marque.objects.all()
    marque = Modele.objects.values('marque_id').distinct()  
    context ={
        "marque_lists": marque,
        "marque_list" : marques,
        "form" : form,    
        
        "ville" : ville,       
    } 
    if request.method == "POST":
        form = SignupForm(request.POST,request.FILES)  
        if form.is_valid():           
            form.save()
            return redirect("index")
        else:
            form = SignupForm
    return render(request, "inscription.html",context=context)

def logout_user(request):
    logout(request)
    return redirect('index')
   
def modele(request):
    marque = request.GET.get('marque')    
    print(marque)
    modele = Modele.objects.filter(marque=marque)
    context={
        "modeles" : modele
    }
    return render(request, 'partiel/modele_de_voiture.html', context)

def check_password(request):
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 != password2 or password2 != password1:
        return HttpResponse("<div style='color: red; font-size: 20px;'>les mots passes sont pas pareil")
    return HttpResponse("<div style='color:#00ff1A; font-size: 20px;'>les mots passes sont pareil") 

def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("<div style='color: red; font-size: 20px;'>L'email est déjà utiliser")
    else:
        return HttpResponse("<div style='color:#00ff1A; font-size: 20px;'>L'email est utilisable.")