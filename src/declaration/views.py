import random
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render
from compte.models import Marque, Modele, Garage
from declaration.form import constatform

@csrf_protect
def declaration(request):
    csrfContext = RequestContext(request)
    context={}
    form = constatform() 
    marques = Marque.objects.all()
    marque = Modele.objects.values('marque_id').distinct()  
    if request.method == "POST":
        form = constatform(request.POST,request.FILES) 
        if form.is_valid():                                          
            form.save()
            return redirect("garage")
        else:                  
            form = constatform()        
    context = {"form": form, 
                "marque_lists": marque,
                "marque_list" : marques,
                "form" : form,                 
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
    u = random.randint(1,50)
    garage = Garage.objects.all()
    garage = Garage.objects.get(id=u) 
    print(garage)  
    context =  {"garages" : garage}
    return render(request, "garage.html", context)