from django.shortcuts import render


def index(request):
    return render(request, "index.html", {'navbar': 'index'})

def formule(request):
    return render(request, "formule.html", {'navbar': 'formule'})

def sinistre(request):
    context={'navbar': 'sinistre'}
    return render(request, "sinistre.html",context)



    