from compte.models import Marque, Modele, Departement, Region, Ville, Remorque, Garage
from pathlib import Path
import random
import json





def inscription_ville():
    villes = []  
    commune = Ville.objects.all()
       
    for i in range(22181): 
        add_ville = commune[i].nom + str(i) 
        villes.append(add_ville)       
   
    json_data = {
        "villes": villes
    }

    with open('city.json', 'w',) as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=True)   


prenoms = ["Axel","Adrien","Augustin","Amaury","Ayoub","Bastien","Arthur","Alban","Alexis","Antoine","Auguste","Benjamin",
           "Achille","Adam","Alexandre","Baptiste","Aaron","Antonin","Armand","Basile","Elias","Diego","Esteban","Dylan","David",
           "Emile","Daniel","Erwan","Charles","Clement","Corentin","Elie","Enzo","Gabin","Felix","Evan","Gabriel","Gaspard","Julien",
           "Idriss","Isaac","Joseph","Jules","Jean","Hugo","Léo","Lucien","Mathias","Marin","Marius","Lorenzo","Mael","Maxime","Lois",
           "Louis","Mateo","Leonard","Luca","Marcel","Mathis","Léon","Lucas","Marceau","Matteo","Martin","Pierre","Quentin",
           "Nicolas","Raphaël","Oscar","Paul","Noé","Pablo","Nathanael","Rafael","Nathan","Romain","Theo","Samuel","Simon",
           "Robin","Romeo","Victor","Youssef","Tiago","Tom","Tristan","William","Abel","Thibault","Thomas","Valentin","Adem","Ali"
           "Ahmed","Alessio","Anas","Amir","Amine","Aylan","Bilal","Aymen","Ayden","Charly","Elio","Ethan","Eliot","Eliott","Sebastien","Serge","Steve"
           "Richard","Antoine"]


noms_de_famille = ["Martin","Bernard","Thomas","Petit","Robert","Richard","Durand","Dubois","Moreau","Laurent",
           "Simon","Michel","Lefebvre","Leroy","Roux","David","Bertrand","Morel","Fournier","Girard","Bonnet",
           "Dupont","Lambert","Fontaine","Rousseau","Vincent","Muller","Lefevre","Faure","Andre","Mercier","Blanc",
           "Guerin","Boyer","Garnier","Chevalier","Francois","Legrand","Gauthier","Garcia","Perrin","Robin","Clement",
           "Morin","Henry","Roussel","Mathieu","Gautier","Masson","Marchand","Duval","Denis","Dumont","Marie","Lemaire",
           "Noel","Meyer","Dufour","Meunier","Brun","Blanchard","Giraud","Joly","Riviere","Lucas","Brunet","Gaillard",
           "Barbier","Arnaud","Martinez","Gerard","Roche","Renard","Schmitt","Roy","Leroux","Colin","Vidal","Caron",
           "Picard","Roger","Fabre","Aubert","Lemoine","Renaud","Dumas","Lacroix","Olivier","Philippe","Bourgeois",
           "Pierre","Benoit","Rey","Leclerc","Payet","Rolland","Leclercq","Guillaume","Lecomte","Lopez","Jean","Dupuy",
           "Guillot","Hubert","Berger","Carpentier","Sanchez","Dupuis","Moulin","Louis","Deschamps","Huet","Vasseur",
           "Perez","Boucher","Fleury","Royer","Klein","Jacquet","Adam","Paris","Poirier","Marty","Aubry","Guyot","Carre",
           "Charles","Renault","Charpentier","Menard","Maillard","Baron","Bertin","Bailly","Herve","Schneider","Fernandez",
           "Le Gall","Collet","Leger","Bouvier","Julien","Prevost","Millet","Perrot","Daniel","Le Roux","Cousin","Germain",
           "Breton","Besson","Langlois","Remy","Le Goff","Pelletier","Leveque","Perrier","Leblanc","Barre","Lebrun","Marchal",
           "Weber","Mallet","Hamon","Boulanger","Jacob","Monnier","Michaud","Rodriguez","Guichard","Gillet","Etienne","Grondin",
           "Poulain","Tessier","Chevallier","Collin","Chauvin","Da Silva","Bouchet","Gay","Lemaitre","Benard","Marechal","Humbert",
           "Reynaud","Antoine","Hoarau","Perret","Barthelemy","Cordier","Pichon","Lejeune","Gilbert","Lamy","Delaunay",
           "Pasquier","Carlier","Laporte"]

def creation_de_garage():
    nom_de_garage = ["du Sud", "de l'Ouest", "de l'Est", "du Nord", "Centrale","du goul","du chevalier", "deLanie","de l'impro", "du Kass",
                     "du Rousseau","Michelin","Peugeot","Renauld","AssurPlus","Touche à tout","Mecar","Raremenvuca","Phantom",
                     "AutoSpa","Garage Vroum","En Voiture Simone !","Le Carage","AutoHosto","AutoFix","4x4 Experts","Garages AutoPros",
                     "Moteur Master","Réparations Rapides","AutoLabo","Holy Motors","Pause Technique","Atelier Auto",
                     "Les Frères Garagistes","SudAuto","Mister Mécano","AutoRep Express","Nation Auto","Mécanocity","MécanoMobile",
                     "AutoNomade","Mécanauto","Speed Réparations","Mécanicar","de l'ours","de Popi","de Feu","Unisson"]
    
    nom_des_rues = ["de la Liberté", "des Champs-Élysées", "du Bois", "de la Paix", "de la Gare", "de la République","jean jaurès",
       "jean moulin","léon gambetta","général leclerc","maréchal foch","jules Ferry","georges clémenceau","du Verne",
       "de la Rivolas","de la ferme","des fossés","de la promenade","des Tilleuls","du Moulin","de Sur Prele",
       "du Dorteur Voste","de Tre la Ville","du Lavoir","à Billiat","à Injoux-Génissiat","à Leaz","le village",
       "louis Pasteur","victor Hugo","Jean Jaurès","Jean Moulin","Léon Gambetta","général Leclerc","maréchal Foch",
       "Jules Ferry","georges Clémenceau","de l'Europe","Gambetta","Louis Paster","de la Vibora","de la Victoire",
       "de la Folie","artur Dubois","des jardins","du château","de la fontaine","du stade","de l'église","de la Mairie"
       ,"de la Gare","des écoles"]
    
    files = Path.cwd() / "compte/remorqueurs.json"
    with open(files, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    
   
    commune = Ville.objects.all()
    garages = []
    i=0
    
    for row in datas:

        add_ville = commune[i].code_commune        
        garage = {
        "Garage": "Garage " + random.choice(nom_de_garage),
        "adresse": str(random.randint(1, 100)) +  random.choice([" rue "," avenue "," boulevard "," chemin "," Chaussée "," allée "," place "," villa "," voie "," promenade "])+ random.choice(nom_des_rues),        
        "tel": "0" + str(random.randint(6, 9)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)),
        "remorque": row[str("nom")],
        "lieux": add_ville,
        }    
        print(garage)
        garages.append(garage)
        i=i+1

    json_data = {
        "garages": garages
    }
    with open('garages.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=True)

def remorqueur():    
    remorqueurs = []

    for i in range(35734):
        remorqueur = {           
        "nom": random.choice(noms_de_famille)+str(i),
        "prenom": random.choice(prenoms),
        "plaque": chr(random.randint(ord('A'), ord('Z')))+ chr(random.randint(ord('A'), ord('Z')))+ str(random.randint(100, 999)) + chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z'))),      
        }      
        remorqueurs.append(remorqueur)

    json_data = {
        "remorqueurs": remorqueurs
    }
    with open('remorqueurs.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4,  ensure_ascii=False, sort_keys=True)

def insert_remorqueur():
    file = Path.cwd() / "compte/remorqueurs.json"
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    i=0    
    for row in datas:        
        remorqueur = Remorque(id=None,nom=row[str("nom")],prenom=row["prenom"],plaque=row["plaque"])
        i=i+1
        remorqueur.save()

def voiture():
    file = Path.cwd() / "compte/voiture.json"
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
        
    for row in datas:     
        marq = Marque(nom=row['marque'])
        marq.save()     
        for mod in row['models']:
            try:
                mod = Modele(id=None, modele=mod, marque=marq)
                mod.save()
            except:
                print(mod)

def departement():
    file = Path.cwd() / "compte/departement.json"
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)

    for row in datas:     
        region = list(row.keys())[0]   
        reg = Region( nom = region)
        reg.save()         
    
        for i in row[region]:         
            departement = i['name']         
            code = i['code']         
            dep = Departement(nom = departement, code = code, region =reg)
            dep.save()

def villa():
    # datas = p.read_csv("communes.csv")
    file = Path.cwd() / "compte/communes.json"
    with open(file, 'r', encoding='utf-8') as f:    
         datas = json.load(f)           

    for row in datas:
        try:
            cod=str(row["Code_postal"])[0:2]
            dep = Departement.objects.get(code=int(cod))    
            ville = Ville(code_commune=row["Code_commune_INSEE"],nom=row["Nom_commune"], code_postal=row["Code_postal"], departement=dep) 
            ville.save()      
          
        except:
            print(f"{ville} du departement {dep} ne pas pu être inscrit {cod}") 

def insert_garages():
    i=0
    file = Path.cwd() / "compte/garages.json"
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)

    for row in datas:       
        garages = Garage(id=None,slug=row[str("Garage")],nom=row["Garage"],numberPhone=row["tel"],adresse=row['adresse'],remorque=Remorque.objects.get(nom=row["remorque"]),lieu=Ville.objects.get(code_commune=row["lieux"]))
        print(garages)
        i=i+1
        garages.save()

def action():
    departement()
    voiture()
    villa()
    insert_remorqueur()
    insert_garages()
