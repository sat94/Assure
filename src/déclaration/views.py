from django.shortcuts import redirect, render
from compte.models import Ville, Marque, Modele
from déclaration.form import constatform



def declaration(request):
    context={}
    form = constatform() 
    ville = Ville.objects.all() 
    marques = Marque.objects.all()
    marque = Modele.objects.values('marque_id').distinct() 
    ville = Ville.objects.all() 
    if request.method == "POST":
        form = constatform(request.POST,request.FILES) 
        if form.is_valid():                           
            form.save()
            return redirect("garage")
        else:
            print("c'est faux")
            form = constatform()
    context = {"form": form, 
                "marque_lists": marque,
                "marque_list" : marques,
                "form" : form,   
                "ville" : ville,                                      
               }
    return render(request, "declaration.html",context)

def modelee(request):
    marque = request.GET.get('marque')    
    print(marque)
    modele = Modele.objects.filter(marque=marque)
    context={
        "modeles" : modele
    }
    return render(request, 'partiel/modele_de_voitur.html', context)

def garage(request):
    return render(request, "garage.html")