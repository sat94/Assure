from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, formule, sinistre
from compte.views import *
from déclaration.views import *
from profils.views import profils
from main import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", index, name="index"),
    path('formule', formule, name="formule"),
    path('sinistre', sinistre, name="sinistre"),
    path('compte/', include ('django.contrib.auth.urls')),
    path('compte/inscription', inscription, name='inscription'),  
    path('sos/', declaration, name='declaration'),
    path('profils/', profils, name='profils'),       
    path('compte/voiture/modele', modele, name='voiture'),
    path('sos/modele', modelee, name='sos'),
    path('garage', garage, name="garage")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpartterns = [
    path('check_email/', check_email, name='check-email'),
    path('check_password/',check_password, name='check_password'),    
]

urlpatterns += htmx_urlpartterns 