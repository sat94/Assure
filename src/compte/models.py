from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django_resized import ResizedImageField



class MyUserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        email = self.normalize_email(email)         
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, email=None, password=None):
        email = self.normalize_email(email)            
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
   
typee = [
    ('Berline', 'berline'),
    ('Coupée', 'Coupée'),
    ('Hayon', 'Hayon'),
    ('Pick-up', 'Pick-up'),
    ('Crossover', 'Crossover'),
    ('SUV', 'SUV'),
    ('Fourgonettes','Fourgonettes'),
    ('Cabriolets','Cabriolets'),
    ('Roadsters','Roadsters'),
    ('Targa', 'Targa'),
]

couleur = [
    ('Rouge', 'Rouge'),
    ('Gris', 'Gris'),
    ('Blanche', 'Blanche'),
    ('Bleu', 'Bleu'),
    ('Noire', 'Noire'),
    ('Jaune', 'Jaune'),
    ('Verte', 'Verte'),
    ('Maron', 'Maron'),
    ('Violette', 'Violette'),
    ('Rose', 'Rose'),
    ('Beige', 'Beige'),
    ('Silver', 'Silver'),    
]
permi = [
    ('Client', 'Client'),
    ('Commercial', 'Commercial'),
    ('Administrateur', 'Administrateur'),
]

sexe = [
    ('homme', 'homme'),
    ('femme', 'femme'),
]

contrat = [
    ('Formule 1', 'Formule 1'),
    ('Formule 2', 'Formule 2'),
    ('Formule 3', 'Formule 3'),
    ('Commercial', 'Commercial'),
    ('Administrateur', 'Administrateur'),      
]

class MyUser(AbstractBaseUser): 
    email = models.EmailField(unique=True, max_length=30, blank=False)    
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    nbpermis = models.CharField(max_length=20,null=True, blank=True)
    age = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    sexe = models.CharField(choices=sexe,max_length=20)
    slug = models.SlugField(max_length=20)
    photo = ResizedImageField(size=[250, 350], quality=85, upload_to='photo', null=True, blank=True)
    adresse = models.CharField(max_length=200)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 10)   
    ville = models.OneToOneField("compte.ville", on_delete=models.SET_NULL, null=True, blank=True)
    postal = models.IntegerField(null=True, blank=True)   
    Nbcontrat = models.IntegerField(validators = [phone],null=True, blank=True)
    Contrat = models.ForeignKey("compte.Formule", on_delete=models.SET_NULL, null=True, blank=True)
    permission = models.CharField(choices=permi, max_length=20, default="Client")
    jeune = models.BooleanField(default=False)
    commercial = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    marque = models.ForeignKey('compte.Marque', on_delete=models.SET_NULL, max_length=20, null=True, blank=True)
    modeles = models.ForeignKey('compte.Modele', on_delete=models.SET_NULL, max_length=20, null=True, blank=True)
    plaque = models.CharField(max_length=20)
    photo_voiture = ResizedImageField(size=[250, 350], quality=85, upload_to='photo', null=True, blank=True)
    typee = models.CharField(choices=typee, max_length=20)
    annee = models.DateField( auto_now=False, auto_now_add=False, null=True, blank=True)
    couleur = models.CharField(choices=couleur, max_length=20)
    chevaux = models.CharField(max_length=3, null=True, blank=True) 

    USERNAME_FIELD = "email"
    objects = MyUserManager()
    
    def __str__(self):       
        return self.email      
     
 
    def save(self, *args, **kwargs):
        self.Nbcontrat = id(MyUser)
        self.slug = slugify(self.nom)            
        super().save(*args, **kwargs)    
    

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True  

class Formule(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.nom   
   
class Marque(models.Model):   
    nom = models.CharField(max_length=20, unique=True)  

    def __str__(self):
        return f"{self.nom}"

class Modele(models.Model): 
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL,  max_length=20, null=True, blank=True)
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom   

class Garage(models.Model):
    slug = models.SlugField(max_length=20)
    nom = models.CharField(max_length=20)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 10) 
    adresse = models.CharField(max_length=200)    
    lieu = models.OneToOneField("compte.Ville", on_delete=models.SET_NULL, null=True, blank=True)
    remorque =  models.OneToOneField("compte.Remorque", on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)            
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.slug

class Remorque(models.Model):
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    plaque = models.CharField(max_length=20)
   

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']
   

class Accident(models.Model):
    description = models.CharField(max_length=90) 
    
    def __str__(self):
        return self.description
   

dégats = [
    ("1", "dégat sur mon véhicule"),
    ("2", "dégat sur l'autre véhicule"),
    ("3", "dégat sur véhicule autre que A et B"),
    ("4", "dégat sur objet autre que A et B"),
]
assurance=[
    ("1","Assureplus"),
    ("2","Direct Assurance"),
    ("3","Eurofils"),
    ("4","MMA"),
    ("5","Active Assurance"),
    ("6","Acomme Assurance"),
    ("7","MAAF"),
    ("8","Allianz"),
    ("9","L'olivier Assurance"),
    ("10","Leocare"),
    ("11","SOS Malus"),
    ("12","Lablette"),
    ("13","AXA"),
    ("15","Matmut"),
    ("16","Cardif"),
    ("17","SwissLife"),
    ("18","MAIF"),
    ("19","AMF"),
    ("20","LCL Assurance"),
    ("21","GROUPAMA"),
    ("22","April"),
    ("23","GENERAL ASSURANCE"),
    ("24","AVIVA"),
    ("25","Banque Postale"),
    ("26","Carrefour ASSURANCE"),
    ("27","AGPM")
]
ou = [
    ("devant","devant"),
    ("arriere","arriere"),
    ("coter droit", "coter droit"),
    ("coter gauche", "coter gauche"),
]

class Constat(models.Model):
    blesse = models.BooleanField(default=False)
    personne = models.OneToOneField(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=50 , null=True, blank=True)
    prenom = models.CharField(max_length=50 , null=True, blank=True)
    age =  models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) 
    mail = models.EmailField(null=True, blank=True) 
    adresse = models.CharField(max_length=50 , null=True, blank=True)
    code_postal = models.IntegerField(null=True, blank=True)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")    
    tel = models.CharField(validators = [phone], max_length = 10, null=True, blank=True)
    voiture = models.ForeignKey("compte.Marque", on_delete=models.SET_NULL, null=True, blank=True)
    modeles = models.ForeignKey("compte.Modele", on_delete=models.SET_NULL, max_length=20, null=True, blank=True)
    typee = models.CharField(choices=typee, max_length=20, null=True, blank=True)
    couleur = models.CharField(choices=couleur, max_length=20, null=True, blank=True)
    plaque = models.CharField(max_length=20, null=True, blank=True)
    nbpermis = models.CharField(max_length=20, null=True, blank=True)
    nbcontrat = models.CharField(max_length=20, null=True, blank=True)    
    assurance = models.CharField(choices=assurance, max_length=35, null=True, blank=True)
    circonstance = models.ManyToManyField(Accident, max_length=20)
    nbCirconstance = models.IntegerField(null=True, blank=True)
    degatsA = models.CharField(choices=dégats, max_length=20, null=True, blank=True)
    degatsB = models.CharField(choices=dégats, max_length=20, null=True, blank=True)
    degatouA = models.CharField(choices=ou,max_length=20, null=True, blank=True)
    degatouB = models.CharField(choices=ou,max_length=20, null=True, blank=True)
    degatautre = models.BooleanField(default=False, null=True, blank=True)  
    lieu = models.OneToOneField("compte.Ville", on_delete=models.SET_NULL, null=True, blank=True)
    degat_vehicule_a=models.CharField(max_length=50,null=True, blank=True)
    degat_vehicule_b=models.CharField(max_length=50,null=True, blank=True)
    dossier_en_cour:models.BooleanField(default=True)
    commentaireA= models.CharField(max_length=200,null=True, blank=True)
    commentaireB = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField( auto_now=False, auto_now_add=False, null=True, blank=True)
    photo = ResizedImageField(size=[250, 350], quality=85, upload_to='photo', null=True, blank=True)  
    temoin = models.CharField(max_length=50,null=True, blank=True)
    signature = models.BooleanField(default=False)
    
  
    
 

class Region(models.Model):
    nom = models.CharField(max_length=20)    
    def __str__(self):
        return self.nom
    class Meta:
       ordering = ['nom']

class Departement(models.Model): 
    region = models.ForeignKey(Region, on_delete=models.SET_NULL,null=True, blank=True)
    nom = models.CharField(max_length=20) 
    code = models.CharField(max_length=4)
    
    def __str__(self):
        return self.nom
    class Meta:
        ordering = ['nom']

class Ville(models.Model):    
    code_commune = models.CharField(max_length=5, unique=True)
    nom = models.CharField(max_length=20)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    code_postal = models.CharField(max_length=5)

      
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']


 