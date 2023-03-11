from django.contrib import admin
from compte.models import MyUser, Garage, Constat,Modele, Marque,Formule,Accident
from django.contrib.auth.models import Group


admin.site.site_header="Administrateur Assure Plus"
admin.site.register(MyUser)
admin.site.unregister(Group)

@admin.register(Garage, Constat, Modele, Marque, Formule, Accident)
class PersonAdmin(admin.ModelAdmin):
    pass

