from django.contrib import admin
from compte.models import MyUser, Garage, Constat, Remorque, Modele, Marque, Region, Formule, Departement, Ville, Accident
from django.contrib.auth.models import Group



@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code' )

  

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display =('nom', 'code_postal', 'departement')
    search_fields=('nom',)

admin.site.site_header="Administrateur Assure Plus"
admin.site.register(MyUser)
admin.site.unregister(Group)

@admin.register(Garage, Constat, Remorque, Modele, Marque, Formule, Region, Accident)
class PersonAdmin(admin.ModelAdmin):
    pass

