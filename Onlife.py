## Importation des bibliothèques
import pygame
from pygame.locals import *
import pygame_menu
import random
from random import randint
from game import Game

## Mise en place de la fenêtre, des listes, des images, des couleurs et une variable

#Création de la fenêtre
width = 1200
height = 800
background_colour = (255,153,153)
fenetre = pygame.display.set_mode((width,height))
fenetre.fill(background_colour)
gamename = pygame.display.set_caption("Onlife")

# Couleurs
color = (255,255,255)
color2= (0,0,0)
color_light = (170,170,170)
color_dark = (100,100,100)
color_red = (249,113,113)
color_dred = (220,20,60)
color_bred = (207,69,96)
color_crimson = (220,20,60)
color_spring = (60,179,113)
color_sea = (143,188,143)
color_blue = (0,0,100)
color_navy = (0,0,139)
game_colour1 = (105,105,105)
game_colour2 = (128,128,128)

# Police des textes
minifont = pygame.font.SysFont('comicsansms',25)
minifont2 = pygame.font.SysFont('comicsansms',30)
smallfont = pygame.font.SysFont('comicsansms',35)
mediumfont = pygame.font.SysFont('comicsansms',40)
bigfont = pygame.font.SysFont('comicsansms',50)
bigfont2 = pygame.font.SysFont('comicsansms',60)

# Theme personalisé pour les menus
mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.background_color=(255,204,204)
mytheme.title_background_color=(255,153,153)
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
mytheme.title_font=pygame_menu.font.FONT_COMIC_NEUE
mytheme.title_font_color=(0,0,0)
mytheme.widget_font=pygame_menu.font.FONT_NEVIS
mytheme.widget_font_color=(0,0,0)

# Images de fond
back = pygame.image.load('image1.jpg') #Page mini-jeu
background =pygame.transform.scale(back,(width,height))
fondbien=pygame.image.load('Terminal.jpg') #Page bien-être
fondbienetre=pygame.transform.scale(fondbien,(1150,750))

# Images de personnages
femme1=pygame.image.load('Femme1.png').convert_alpha()
femme2=pygame.image.load('Femme2.png').convert_alpha()
femme3=pygame.image.load('Femme3.png').convert_alpha()
femme4=pygame.image.load('Femme4.png').convert_alpha()

homme1=pygame.image.load('Homme1.png').convert_alpha()
homme2=pygame.image.load('Homme2.png').convert_alpha()
homme3=pygame.image.load('Homme3.png').convert_alpha()
homme4=pygame.image.load('Homme4.png').convert_alpha()
homme5=pygame.image.load('Homme5.png').convert_alpha()

# Images de décoration
icon = pygame.image.load('icon.png').convert_alpha()
iconfond =pygame.transform.scale(icon,(250,250))
gameicon = pygame.display.set_icon(icon)
maternelle2=pygame.image.load('Maternelle.png').convert_alpha()
maternelle=pygame.transform.scale(maternelle2,(925,450))
primaire2=pygame.image.load('Primaire.png').convert_alpha()
primaire=pygame.transform.scale(primaire2,(925,450))
college2=pygame.image.load('College.png').convert_alpha()
college=pygame.transform.scale(college2,(925,450))
lycee2=pygame.image.load('Lycee.png').convert_alpha()
lycee=pygame.transform.scale(lycee2,(925,450))
school2=pygame.image.load('school.png').convert_alpha()
school=pygame.transform.scale(school2,(975,500))
interview=pygame.image.load('interview.png').convert_alpha()
bannerright2=pygame.image.load('bannerright2.png').convert_alpha()
bannerright=pygame.transform.scale(bannerright2,(400,600))
bannerleft2=pygame.image.load('bannerleft2.png').convert_alpha()
bannerleft=pygame.transform.scale(bannerleft2,(400,600))
bannermiddle2=pygame.image.load('bannermiddle2.png').convert_alpha()
bannermiddle=pygame.transform.scale(bannermiddle2,(465,200))
traveling1=pygame.image.load('traveling.jpeg')
traveling=pygame.transform.scale(traveling1,(550,580))

# Images des pays
france1=pygame.image.load('france.png')
france=pygame.transform.scale(france1,(200,120))
espagne1=pygame.image.load('espagne.png')
espagne=pygame.transform.scale(espagne1,(200,120))
etatsunis1=pygame.image.load('etatsunis.png')
etatsunis=pygame.transform.scale(etatsunis1,(200,120))
italie1=pygame.image.load('italie.png')
italie=pygame.transform.scale(italie1,(200,120))
mexique1=pygame.image.load('mexique.png')
mexique=pygame.transform.scale(mexique1,(200,120))
allemagne1=pygame.image.load('allemagne.png')
allemagne=pygame.transform.scale(allemagne1,(200,120))
thailande1=pygame.image.load('thailande.png')
thailande=pygame.transform.scale(thailande1,(200,120))
nouvellezelande1=pygame.image.load('nouvellezelande.png')
nouvellezelande=pygame.transform.scale(nouvellezelande1,(200,120))
angleterre1=pygame.image.load('angleterre.png')
angleterre=pygame.transform.scale(angleterre1,(200,120))
japon1=pygame.image.load('japon.png')
japon=pygame.transform.scale(japon1,(200,120))
grece1=pygame.image.load('grece.png')
grece=pygame.transform.scale(grece1,(200,120))
chine1=pygame.image.load('chine.png')
chine=pygame.transform.scale(chine1,(200,120))
malaisie1=pygame.image.load('malaisie.png')
malaisie=pygame.transform.scale(malaisie1,(200,120))
russie1=pygame.image.load('russie.png')
russie=pygame.transform.scale(russie1,(200,120))
portugal1=pygame.image.load('portugal.png')
portugal=pygame.transform.scale(portugal1,(200,120))
canada1=pygame.image.load('canada.png')
canada=pygame.transform.scale(canada1,(200,120))
pologne1=pygame.image.load('pologne.png')
pologne=pygame.transform.scale(pologne1,(200,120))
paysbas1=pygame.image.load('paysbas.png')
paysbas=pygame.transform.scale(paysbas1,(200,120))
australia1=pygame.image.load('australia.png')
australia=pygame.transform.scale(australia1,(200,120))
austria1=pygame.image.load('austria.png')
austria=pygame.transform.scale(austria1,(200,120))

# Listes vides pour contenir le choix du domicile, du transport et des animaux de compagnie
choixdomicile=[]
choixtransport=[]
choixanimal=[]

# Listes de noms
nomsfemmes=["Clara Cuoghi","Aurélie Gallet","Jamie Robin","Charlie Roussel","Riley Dumont","Ambre Meyer","Cléa Blanchard","Iris Martinez","Elie Roux","Manon Roger","Alice Fabre","Lina Lacroix","Maria Rolland","Rose Jacob","Lucie Rodriguez"]
nomshommes=["Rayane Dahmoul","Haroun Abidi","Alex Martin","Claude Thomas","Sam Robert","Max Durand","Maxime Dubois","Adrien Moreau","Alexis Simon","Bastien Lopez","Arthur Fournier","Louis Girard","Oscar Clement","Ethan Blanc","Nathan Muller"]

# Liste des personnages
imagesfemmes=[femme1,femme2,femme3,femme4]
imageshommes=[homme1,homme2,homme3,homme4,homme5]

# Listes des établissements, des spécialités et des métiers
listematernelle=["Ecole maternelle Béré","Ecole maternelle Le Coudray","Ecole maternelle Henri Bergson","Ecole maternelle Jules Ferry","Ecole maternelle Claude Monet","Ecole maternelle Prince Bois","Ecole maternelle Le Bourgeau","Ecole maternelle du Massif","Ecole maternelle Molière","Ecole maternelle du Centre"]
listeprimaire=["Ecole primaire Guillaume Apollinaire","Ecole primaire Michel Servet","Ecole primaire Albert Barraud","Ecoles primaire les Néréides","Ecole primaire Jean Jaurès","Ecole primaire Jacques Prévert","Ecole primaire Charles Perrault","Ecole primaire La Clé des Champs","Ecole primaire Les Nondales","Ecole primaire L'Arbre Enchanté"]
listecollege=["Collège Chaptal","Collège Plaisance","Collège Jean Giono","Collège les Fontainettes","Collège Victor Hugo","Collège des Trois Vallées","Collège la Sablière","Collège Antoine de Saint-Exupéry","Collège Claude Nicolas le Doux","Collège Les Franchises"]
listelycee=["Lycée Jean Rostand","Lycée Henri Vincenot","Lycée Camille Claudel","Lycée Pasteur","Lycée Gustave Eiffel","Lycée Voltaire","Lycée Parc des Loges","Lycée Martin Luther King","Lycée Honoré Romane","Lycée Jean Monnet"]
listeuniversite=["Commerce","Ingénieur","Lettres","Arts","Politique","Sc.Sociales","Droit","Architecture","Médecine"]
dicometiers=[["Caissier",1750],["Commercial",4108],["Acheteur",3500],["Ag.Immobilier",3500],["Ag.Marketing",5083],["Aéronautique",5100],["Chimie",5500],["Environnement",2000],["Génie Civil",4750],["Mécanique",2300],["Ecrivain",2767],["Libraire",2000],["Traducteur",2500],["Editeur",5000],["Enseignant",3500],["Illustrateur",3986],["Photographe",1430],["Sculpteur",1800],["Peintre",4400],["Galeriste",2240],["Ministre",14900],["Politologue",1430],["Diplomate",3700],["Maire",8454],["Parlementaire",8757],["Démographe",3600],["Ethnologue",2500],["Historien",1500],["Sociologue",2160],["Assistant soc.",1700],["Avocat",2600],["Juge",4447],["Notaire",8700],["Huissier",8000],["Greffier",2580],["Architecte",3300],["Urbaniste",2800],["Décorateur",4000],["Installateur",2000],["Coloriste",1700],["Médecin",10684],["Pharmacien",3850],["Psychologie",3200],["Chirurgien",11500],["Infirmier",1800]]

# Listes des articles
listedomicile=[["Studio - 1",98],["Studio - 2",127],["Studio - 3",75],["Studio - 4",82],["Studio - 5",250],["Appart - 1",249],["Appart - 2",450],["Appart - 3",330],["Appart - 4",279],["Appart - 5",427],["Maison - 1",985],["Maison - 2",824],["Maison - 3",675],["Maison - 4",310],["Maison - 5",639],["Villa - 1",1690],["Villa - 2",2780],["Villa - 3",3150],["Villa - 4",1330],["Villa - 5",1490]]
listetransport=[["Vélo - 1",1.75],["Vélo - 2",4.6],["Moto - 1",5.9],["Moto - 2",10.3],["Berline - 1",15.5],["Berline - 2",22.3],["Break - 1",16.6],["Break - 2",19.2],["Monospace - 1",23.6],["Monospace - 2",28.1],["Citadines - 1",16.2],["Citadines - 2",22.9],["4x4 - 1",29],["4x4 - 2",31.8],["Limousine - 1",47],["Limousine - 2",72],["Bateau - 1",159],["Bateau - 2",385],["Jet Privé - 1",2950],["Jet Privé - 2",5000]]
listeanimal=[["Chien - 1",1],["Chien - 2",1.5],["Chat - 1",1],["Chat - 2",1.25],["Poisson - 1",0.15],["Poisson - 2",0.25],["Furet - 1",2.5],["Furet - 2",3.25],["Cheval - 1",6],["Cheval - 2",9.75],["Lapin - 1",3.5],["Lapin - 2",4.45],["Hamster - 1",1.7],["Hamster - 2",2.25],["Oiseau - 1",5.25],["Oiseau - 2",8.75],["Poule - 1",0.2],["Poule - 2",0.5],["Cochon - 1",3.75],["Cochon - 2",6.5]]

# Fichier csv des pays
file=open("voyage.csv","r",encoding='UTF-8-sig') #On ouvre le fichier
optionsvoyage=file.readline().rstrip().split(';') # On lit la première ligne, on enlève le \n, on découpe à chaque ; et on met le résultat dans optionsvoyage
lignes=file.readlines() # On lit toutes les lignes
contenuvoyage=[] # On crée une table vide
for ligne in lignes : # On itère la variable ligne sur chaque élément de lignes
    liste=ligne.rstrip().split(';') # On crée la liste sans retour à la ligne
    contenuvoyage.append(liste) # On ajoute la liste obtenue à contenuvoyage
file.close() # On ferme le fichier

# Variables
sexe = 0 # Variable pour le sexe choisis
variableargent = randint(100, 100000) #Variable de l'argent
choixlycee=random.choice(listelycee) # Variable du lycée
choix="" # Variable du choix de la spécialité
choixmetier="" # Variable du choix du métier

#Musique
song1 = "bensound-onceagain.mp3"
song2 = "musiquedefond.mp3"


## Fonction du début du jeu (premier menu)
# Code pour le menu du départ en utilisant la bibliothèque pygame_menu

def depart():
    pygame.mixer.init()
    pygame.mixer.music.load(song1)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    menu = pygame_menu.Menu(800, 1200, 'ONLIFE',theme=mytheme)
    logo= menu.add_image('icon.png')
    menu.add_button('Jouer', sexe)
    menu.add_button('Guide', guide_du_jeu)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(fenetre)


## Fonction du sexe (deuxième menu)
# Code pour faire tourner la fonction menu pour choisir le sexe

def sexe():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(-1)
    ecran = pygame_menu.Menu(800, 1200, 'ONLIFE',theme=mytheme)
    genre = ecran.add_image('femmehomme.png')
    femme = ecran.add_button('Femme',principal_femme)
    homme = ecran.add_button('Homme',principal_homme)
    ecran.add_button('Retour',depart)
    ecran.mainloop(fenetre)


## Fonction guide du jeu
#Fonction pour afficher une présentation du jeu

def guide_du_jeu():
    # Textes
    retour = smallfont.render('retour' , True , color) #Création du texte
    ligne1 = bigfont.render('Bienvenu à Onlife!' , True , color2) #Création du texte
    ligne2 = minifont.render("Le jeu où vous pouvez vivre la vie dont vous avez tant rêvé!", True , color2) #Création du texte
    ligne3 = minifont.render("Vous commencez à l'an 0 avec une somme aléatoire d'argent.", True , color2) #Création du texte
    ligne4 = minifont.render("Pour grandir d'une année, appuyez sur la touche '+ une année'.", True , color2) #Création du texte
    ligne5 = minifont.render("Au fil de votre vie, vous pouvez choisir vos études, votre métier et jouer au mini-jeu.", True , color2) #Création du texte
    ligne6 = minifont.render("Vous avez 100 ans pour vous amuser le plus possible!", True , color2) #Création du texte
    ligne7 = mediumfont.render('Éducation:' , True , color2) #Création du texte
    ligne8 = minifont.render("Vous commencez à 3 ans, vous allez à la maternelle, en primaire, au collège puis au lycée.", True , color2) #Création du texte
    ligne9 = minifont.render("À 19 ans, vous pouvez choisir votre spécialité et à 23 ans, votre métier.", True , color2) #Création du texte
    ligne10 = minifont.render("Vous pouvez ensuite jouer à un mini-jeu complémentaire pour gagner de l'argent.", True , color2) #Création du texte
    ligne11 = mediumfont.render('Propriété:' , True , color2) #Création du texte
    ligne12 = minifont.render("Il y a trois catégories de propriété: 'domicile', 'transport', 'animal'.", True , color2) #Création du texte
    ligne13 = minifont.render("Vous pouvez vous rendre en magasin pour acheter un maximum de 7 articles par catégorie.", True , color2) #Création du texte
    ligne14 = mediumfont.render('Bien-être:' , True , color2) #Création du texte
    ligne15 = minifont.render("Ici, vous pouvez choisir votre voyage pour partir aux quatre coins du monde.", True , color2) #Création du texte

    # Variable pour la boucle guide
    guide=True
    # Boucle pour faire tourner la page du guide
    while guide:
        # Mise en place de l'affichage de la fenêtre
        pygame.display.update()
        fenetreoption = pygame.display.set_mode((width,height))
        fenetreoption.fill(background_colour)
        pygame.draw.rect(fenetreoption, (255,204,204), pygame.Rect(35, 35, width-70, height-70))
        # Détection de la position de la souris
        mouse = pygame.mouse.get_pos()

        # Afficher le texte sur l'écran
        fenetreoption.blit(ligne1, (400,40))
        fenetreoption.blit(ligne2, (50,130))
        fenetreoption.blit(ligne3, (50,170))
        fenetreoption.blit(ligne4, (50,210))
        fenetreoption.blit(ligne5, (50,250))
        fenetreoption.blit(ligne6, (50,290))
        fenetreoption.blit(ligne7, (50,340))
        fenetreoption.blit(ligne8, (50,390))
        fenetreoption.blit(ligne9, (50,430))
        fenetreoption.blit(ligne10, (50,470))
        fenetreoption.blit(ligne11, (50,520))
        fenetreoption.blit(ligne12, (50,570))
        fenetreoption.blit(ligne13, (50,610))
        fenetreoption.blit(ligne14, (50,660))
        fenetreoption.blit(ligne15, (50,710))

        # Bouton retour à la page principale
        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
            pygame.draw.rect(fenetreoption,color_light,[50,50,125,50])
        else:
            pygame.draw.rect(fenetreoption,color_dark,[50,50,125,50])
        fenetreoption.blit(retour , (60,50))

        # Détection d'événements
        for event in pygame.event.get():   # On parcours la liste de tous les événements reçus
            if event.type == QUIT:     # Si un de ces événements est de type QUIT
                guide = False      # On arrête la boucle
                pygame.display.quit() # On ferme le display

            # Vérifie si la souris est cliquée
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Bouton retour
                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                    pygame.display.update()
                    guide=False
                    depart()


## Fonction du magasin
#Fonction pour acheter et revendre des articles

def lemagasin(num,liste,choixliste,sexe,perso,nom,age,argent,salaire,nomlycee,spe,metier,domicile,transport,animaux):
    # Textes
    magasin = bigfont.render('Magasin' , True , color) #Création du texte
    retour = smallfont.render('retour' , True , color) #Création du texte
    maximummag = minifont2.render("Vous n'avez pas assez d'argent ou vous avez atteint le maximum d'articles!" , True , color_dark) #Création du texte
    instructions = minifont2.render("Cliquez pour acheter et recliquez pour revendre à -30%. 7 articles maximum." , True , color_dark) #Création du texte

    # Variables
    erreurmag = 0 # Variable pour le message d'erreur
    listemagasin=liste # La liste de la catégorie d'article varie en fonction de la liste entrée en argument de la fonction lemagasin
    choixmagasin=choixliste # La variable choixmagasin varie en fonction de la variable choixliste entrée en argument de la fonction lemagasin et permet de réguler et détecter les articles déjà achetés
    variableargent=argent # La somme d'argent est determinée en fonction de la somme entrée en argument de la fonction lemagasin

    # Variable pour la boucle magasin
    themagasin=True

    # Boucle pour faire tourner la page du magasin
    while themagasin:
        # Mise en place de l'affichage de la fenêtre
        pygame.display.update()
        fenetremag = pygame.display.set_mode((width,height))
        fenetremag.fill(background_colour)
        # Détection de la position de la souris
        mouse = pygame.mouse.get_pos()

        # Titre
        pygame.draw.rect(fenetremag,color_dark,[230,25,900,100])
        fenetremag.blit(magasin , (580,40))

        # Instructions
        fenetremag.blit(instructions , (65,140))

        # Affichage des options d'articles
        article=0
        largeur=75
        for i in range (2): # Distribution en deux colonnes
            hauteur=200
            for i in range (10): # Chaque colonne comporte 10 articles
                nomdelarticle1 = smallfont.render(listemagasin[article][0] , True , color)#Création du texte
                nomdelarticle2 = smallfont.render(str(listemagasin[article][1])+" K" , True , color)#Création du texte
                # Rectangle de couleur différente pour savoir si l'objet à déjà été acheté
                if listemagasin[article][0] in choixmagasin: # Détection si l'article est déjà acheté
                    pygame.draw.rect(fenetremag,color_dred,[largeur-10,hauteur+5,460,43])
                else:
                    pygame.draw.rect(fenetremag,color_bred,[largeur-10,hauteur+5,460,43])
                fenetremag.blit(nomdelarticle1 , (largeur,hauteur))
                fenetremag.blit(nomdelarticle2 , (largeur+330,hauteur))
                hauteur=hauteur+50
                article=article+1
            largeur=largeur+600

        # Bouton retour à la page propriété
        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
            pygame.draw.rect(fenetremag,color_light,[50,50,125,50])
        else:
            pygame.draw.rect(fenetremag,color_dark,[50,50,125,50])
        fenetremag.blit(retour , (60,50))

        # Blit des erreurs
        if erreurmag == 1:
            fenetremag.blit(maximummag , (60,720))

        # Boucle pour les évènements
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Bouton retour
                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                    pygame.display.update()
                    mag=False
                    if num == 1: # Change le contenu des listes d'articles achetés en fonction de la catégorie d'article
                        principal(sexe,perso,nom,age,variableargent,salaire,nomlycee,spe,metier,choixmagasin,transport,animaux)
                    elif num == 2: # Change le contenu des listes d'articles achetés en fonction de la catégorie d'article
                        principal(sexe,perso,nom,age,variableargent,salaire,nomlycee,spe,metier,domicile,choixmagasin,animaux)
                    elif num == 3: # Change le contenu des listes d'articles achetés en fonction de la catégorie d'article
                        principal(sexe,perso,nom,age,variableargent,salaire,nomlycee,spe,metier,domicile,transport,choixmagasin)

                # Détection choix de l'article
                # --> Détecte d'abords si le joueur a assez d'argent et si l'article est déjà acheté
                # --> Si le joueur possède l'article et souhaite le revendre
                # --> Affiche un message d'erreur si les conditions d'achat ne sont pas respectés
                #1
                if 65 <= mouse[0] <= 460+65 and 205 <= mouse[1] <= 43+205:
                    if variableargent > (listemagasin[0][1]*1000) and len(choixmagasin)<7 and listemagasin[0][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[0][1]*1000)
                        choixmagasin.append(listemagasin[0][0])
                        erreurmag=0
                    elif listemagasin[0][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[0][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[0][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #2
                if 65 <= mouse[0] <= 460+65 and 255 <= mouse[1] <= 43+255:
                    if variableargent > (listemagasin[1][1]*1000) and len(choixmagasin)<7 and listemagasin[1][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[1][1]*1000)
                        choixmagasin.append(listemagasin[1][0])
                        erreurmag=0
                    elif listemagasin[1][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[1][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[1][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #3
                if 65 <= mouse[0] <= 460+65 and 305 <= mouse[1] <= 43+305:
                    if variableargent > (listemagasin[2][1]*1000) and len(choixmagasin)<7 and listemagasin[2][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[2][1]*1000)
                        choixmagasin.append(listemagasin[2][0])
                        erreurmag=0
                    elif listemagasin[2][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[2][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[2][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #4
                if 65 <= mouse[0] <= 460+65 and 355 <= mouse[1] <= 43+355:
                    if variableargent > (listemagasin[3][1]*1000) and len(choixmagasin)<7 and listemagasin[3][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[3][1]*1000)
                        choixmagasin.append(listemagasin[3][0])
                        erreurmag=0
                    elif listemagasin[3][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[3][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[3][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #5
                if 65 <= mouse[0] <= 460+65 and 405 <= mouse[1] <= 43+405:
                    if variableargent > (listemagasin[4][1]*1000) and len(choixmagasin)<7 and listemagasin[4][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[4][1]*1000)
                        choixmagasin.append(listemagasin[4][0])
                        erreurmag=0
                    elif listemagasin[4][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[4][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[4][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #6
                if 65 <= mouse[0] <= 460+65 and 455 <= mouse[1] <= 43+455:
                    if variableargent > (listemagasin[5][1]*1000) and len(choixmagasin)<7 and listemagasin[5][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[5][1]*1000)
                        choixmagasin.append(listemagasin[5][0])
                        erreurmag=0
                    elif listemagasin[5][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[5][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[5][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #7
                if 65 <= mouse[0] <= 460+65 and 505 <= mouse[1] <= 43+505:
                    if variableargent > (listemagasin[6][1]*1000) and len(choixmagasin)<7 and listemagasin[6][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[6][1]*1000)
                        choixmagasin.append(listemagasin[6][0])
                        erreurmag=0
                    elif listemagasin[6][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[6][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[6][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #8
                if 65 <= mouse[0] <= 460+65 and 555 <= mouse[1] <= 43+555:
                    if variableargent > (listemagasin[7][1]*1000) and len(choixmagasin)<7 and listemagasin[7][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[7][1]*1000)
                        choixmagasin.append(listemagasin[7][0])
                        erreurmag=0
                    elif listemagasin[7][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[7][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[7][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #9
                if 65 <= mouse[0] <= 460+65 and 605 <= mouse[1] <= 43+605:
                    if variableargent > (listemagasin[8][1]*1000) and len(choixmagasin)<7 and listemagasin[8][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[8][1]*1000)
                        choixmagasin.append(listemagasin[8][0])
                        erreurmag=0
                    elif listemagasin[8][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[8][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[8][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #10
                if 65 <= mouse[0] <= 460+65 and 655 <= mouse[1] <= 43+655:
                    if variableargent > (listemagasin[9][1]*1000) and len(choixmagasin)<7 and listemagasin[9][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[9][1]*1000)
                        choixmagasin.append(listemagasin[9][0])
                        erreurmag=0
                    elif listemagasin[9][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[9][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[9][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #11
                if 665 <= mouse[0] <= 460+665 and 205 <= mouse[1] <= 43+205:
                    if variableargent > (listemagasin[10][1]*1000) and len(choixmagasin)<7 and listemagasin[10][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[10][1]*1000)
                        choixmagasin.append(listemagasin[10][0])
                        erreurmag=0
                    elif listemagasin[10][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[10][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[10][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #12
                if 665 <= mouse[0] <= 460+665 and 255 <= mouse[1] <= 43+255:
                    if variableargent > (listemagasin[11][1]*1000) and len(choixmagasin)<7 and listemagasin[11][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[11][1]*1000)
                        choixmagasin.append(listemagasin[11][0])
                        erreurmag=0
                    elif listemagasin[11][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[11][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[11][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #13
                if 665 <= mouse[0] <= 460+665 and 305 <= mouse[1] <= 43+305:
                    if variableargent > (listemagasin[12][1]*1000) and len(choixmagasin)<7 and listemagasin[12][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[12][1]*1000)
                        choixmagasin.append(listemagasin[12][0])
                        erreurmag=0
                    elif listemagasin[12][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[12][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[12][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #14
                if 665 <= mouse[0] <= 460+665 and 355 <= mouse[1] <= 43+355:
                    if variableargent > (listemagasin[13][1]*1000) and len(choixmagasin)<7 and listemagasin[13][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[13][1]*1000)
                        choixmagasin.append(listemagasin[13][0])
                        erreurmag=0
                    elif listemagasin[13][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[13][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[13][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #15
                if 665 <= mouse[0] <= 460+665 and 405 <= mouse[1] <= 43+405:
                    if variableargent > (listemagasin[14][1]*1000) and len(choixmagasin)<7 and listemagasin[14][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[14][1]*1000)
                        choixmagasin.append(listemagasin[14][0])
                        erreurmag=0
                    elif listemagasin[14][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[14][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[14][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #16
                if 665 <= mouse[0] <= 460+665 and 455 <= mouse[1] <= 43+455:
                    if variableargent > (listemagasin[15][1]*1000) and len(choixmagasin)<7 and listemagasin[15][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[15][1]*1000)
                        choixmagasin.append(listemagasin[15][0])
                        erreurmag=0
                    elif listemagasin[15][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[15][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[15][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #17
                if 665 <= mouse[0] <= 460+665 and 505 <= mouse[1] <= 43+505:
                    if variableargent > (listemagasin[16][1]*1000) and len(choixmagasin)<7 and listemagasin[16][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[16][1]*1000)
                        choixmagasin.append(listemagasin[16][0])
                        erreurmag=0
                    elif listemagasin[16][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[16][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[16][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #18
                if 665 <= mouse[0] <= 460+665 and 555 <= mouse[1] <= 43+555:
                    if variableargent > (listemagasin[17][1]*1000) and len(choixmagasin)<7 and listemagasin[17][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[17][1]*1000)
                        choixmagasin.append(listemagasin[17][0])
                        erreurmag=0
                    elif listemagasin[17][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[17][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[17][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #19
                if 665 <= mouse[0] <= 460+665 and 605 <= mouse[1] <= 43+605:
                    if variableargent > (listemagasin[18][1]*1000) and len(choixmagasin)<7 and listemagasin[18][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[18][1]*1000)
                        choixmagasin.append(listemagasin[18][0])
                        erreurmag=0
                    elif listemagasin[18][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[18][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[18][0])
                        erreurmag=0
                    else:
                        erreurmag=1
                #20
                if 665 <= mouse[0] <= 460+665 and 655 <= mouse[1] <= 43+655:
                    if variableargent > (listemagasin[19][1]*1000) and len(choixmagasin)<7 and listemagasin[19][0] not in choixmagasin:
                        variableargent = variableargent - (listemagasin[19][1]*1000)
                        choixmagasin.append(listemagasin[19][0])
                        erreurmag=0
                    elif listemagasin[19][0] in choixmagasin:
                        variableargent = variableargent + (listemagasin[19][1]*1000*0.7)
                        choixmagasin.remove(listemagasin[19][0])
                        erreurmag=0
                    else:
                        erreurmag=1


## Fonction du voyage
#Fonction pour pouvoir voyager dans une sélection de 20 pays

def levoyage(pays,sexe,perso,nom,age,argent,salaire,nomlycee,spe,metier,choixdomicile,choixtransport,choixanimaux):
    # Variables
    erreuroptions=0 # Variable pour les erreurs
    erreurargent=0 # Variable pour les erreurs
    laclasse=0 # Variable pour détecter le choix de la classe
    laduree=0 # Variable pour détecter le choix de la durée
    lanourriture=0 # Variable pour détecter le choix du moyen de restauration
    lactivite=0 # Variable pour détecter le choix du nombre d'activités
    letransport=0 # Variable pour détecter le choix du moyen de transport
    variableargent=argent # La somme d'argent est determinée en fonction de la somme entrée en argument de la fonction levoyage

    # Variable pour la boucle voyage
    voyage=True

    # Boucle pour faire tourner la page des options du voyage
    while voyage:
        # Mise en place de l'affichage de la fenêtre
        pygame.display.update()
        fenetrevoyage = pygame.display.set_mode((width,height))
        fenetrevoyage.fill(background_colour)
        # Détection de la position de la souris
        mouse = pygame.mouse.get_pos()

        # Textes
        lepays = mediumfont.render(contenuvoyage[pays][0] , True , color) # Extraction des options de la liste et création du texte
        lepayscode = mediumfont.render(contenuvoyage[pays][1] , True , color) # Extraction des options de la liste et création du texte
        classe = smallfont.render("Classe :" , True , color) # Création du texte
        economy = smallfont.render(optionsvoyage[2] , True , color) # Extraction des options de la liste et création du texte
        business = smallfont.render(optionsvoyage[3] , True , color) # Extraction des options de la liste et création du texte
        first = smallfont.render(optionsvoyage[4] , True , color) # Extraction des options de la liste et création du texte
        duree = smallfont.render("Durée :" , True , color) # Création du texte
        deux = smallfont.render(optionsvoyage[5] , True , color) # Extraction des options de la liste et création du texte
        trois = smallfont.render(optionsvoyage[6] , True , color) # Extraction des options de la liste et création du texte
        quatre = smallfont.render(optionsvoyage[7] , True , color) # Extraction des options de la liste et création du texte
        cinq = smallfont.render(optionsvoyage[8] , True , color) # Extraction des options de la liste et création du texte
        six = smallfont.render(optionsvoyage[9] , True , color) # Extraction des options de la liste et création du texte
        sept = smallfont.render(optionsvoyage[10] , True , color) # Extraction des options de la liste et création du texte
        quatorze = smallfont.render(optionsvoyage[11] , True , color) # Extraction des options de la liste et création du texte
        nourriture = smallfont.render("Nourriture :" , True , color) # Création du texte
        repas = smallfont.render(optionsvoyage[12] , True , color) # Extraction des options de la liste et création du texte
        restaurant = smallfont.render(optionsvoyage[13] , True , color) # Extraction des options de la liste et création du texte
        activite = smallfont.render("Activité :" , True , color) # Création du texte
        activite2 = smallfont.render(optionsvoyage[14] , True , color) # Extraction des options de la liste et création du texte
        activite4 = smallfont.render(optionsvoyage[15] , True , color) # Extraction des options de la liste et création du texte
        activite6 = smallfont.render(optionsvoyage[16] , True , color) # Extraction des options de la liste et création du texte
        activite8 = smallfont.render(optionsvoyage[17] , True , color) # Extraction des options de la liste et création du texte
        activite10 = smallfont.render(optionsvoyage[18] , True , color) # Extraction des options de la liste et création du texte
        transport = smallfont.render("Transport :" , True , color) # Création du texte
        taxis = smallfont.render(optionsvoyage[19] , True , color) # Extraction des options de la liste et création du texte
        chauffeur = smallfont.render(optionsvoyage[20] , True , color) # Extraction des options de la liste et création du texte
        annuler = mediumfont.render("Annuler" , True , color) # Création du texte
        valider = mediumfont.render("Valider" , True , color) # Création du texte
        choixmanquant = minifont2.render("Veuillez sélectionner un choix pour toutes les catégories." , True , color_dark) # Création du texte
        toopoortotravel = minifont2.render("Vous n'avez pas assez d'argent, veuillez annuler." , True , color_dark) # Création du texte

        # Titre
        pygame.draw.rect(fenetrevoyage,color_dred,[300,25,600,80])
        fenetrevoyage.blit(lepays , (325,35))
        fenetrevoyage.blit(lepayscode , (795,35))

        # Classe
        fenetrevoyage.blit(classe , (190,150))
        # Boutons de sélection de la classe
        if laclasse == 1:
            pygame.draw.rect(fenetrevoyage,color_bred,[357,150,178,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[357,150,178,50])
        if laclasse == 2:
            pygame.draw.rect(fenetrevoyage,color_bred,[593,150,170,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[593,150,170,50])
        if laclasse == 3:
            pygame.draw.rect(fenetrevoyage,color_bred,[820,150,175,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[820,150,175,50])
        fenetrevoyage.blit(economy , (370,150))
        fenetrevoyage.blit(business , (605,150))
        fenetrevoyage.blit(first , (835,150))

        # Durée
        fenetrevoyage.blit(duree , (170,250))
        # Boutons de sélection de la durée
        if laduree == 1:
            pygame.draw.rect(fenetrevoyage,color_bred,[340,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[340,254,60,50])
        if laduree == 2:
            pygame.draw.rect(fenetrevoyage,color_bred,[440,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[440,254,60,50])
        if laduree == 3:
            pygame.draw.rect(fenetrevoyage,color_bred,[539,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[539,254,60,50])
        if laduree == 4:
            pygame.draw.rect(fenetrevoyage,color_bred,[638,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[638,254,60,50])
        if laduree == 5:
            pygame.draw.rect(fenetrevoyage,color_bred,[737,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[737,254,60,50])
        if laduree == 6:
            pygame.draw.rect(fenetrevoyage,color_bred,[838,254,60,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[838,254,60,50])
        if laduree == 7:
            pygame.draw.rect(fenetrevoyage,color_bred,[942,254,65,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[942,254,65,50])
        fenetrevoyage.blit(deux , (350,250))
        fenetrevoyage.blit(trois , (450,250))
        fenetrevoyage.blit(quatre , (550,250))
        fenetrevoyage.blit(cinq , (650,250))
        fenetrevoyage.blit(six , (750,250))
        fenetrevoyage.blit(sept , (850,250))
        fenetrevoyage.blit(quatorze , (950,250))

        # Nourriture
        fenetrevoyage.blit(nourriture , (200,350))
        # Boutons de sélection du moyen de restauration
        if lanourriture == 1:
            pygame.draw.rect(fenetrevoyage,color_bred,[440,351,270,53])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[440,351,270,53])
        if lanourriture == 2:
            pygame.draw.rect(fenetrevoyage,color_bred,[755,351,220,53])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[755,351,220,53])
        fenetrevoyage.blit(repas , (455,350))
        fenetrevoyage.blit(restaurant , (770,350))

        # Activités
        fenetrevoyage.blit(activite , (225,450))
        # Boutons de sélection du nombre d'activités
        if lactivite == 1:
            pygame.draw.rect(fenetrevoyage,color_bred,[460,450,50,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[460,450,50,50])
        if lactivite == 2:
            pygame.draw.rect(fenetrevoyage,color_bred,[560,450,50,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[560,450,50,50])
        if lactivite == 3:
            pygame.draw.rect(fenetrevoyage,color_bred,[660,450,50,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[660,450,50,50])
        if lactivite == 4:
            pygame.draw.rect(fenetrevoyage,color_bred,[760,450,50,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[760,450,50,50])
        if lactivite == 5:
            pygame.draw.rect(fenetrevoyage,color_bred,[867,450,53,50])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[867,450,53,50])
        fenetrevoyage.blit(activite2 , (475,450))
        fenetrevoyage.blit(activite4 , (575,450))
        fenetrevoyage.blit(activite6 , (675,450))
        fenetrevoyage.blit(activite8 , (775,450))
        fenetrevoyage.blit(activite10 , (875,450))

        # Transport
        fenetrevoyage.blit(transport , (260,550))
        # Boutons de sélection du moyen de transport
        if letransport == 1:
            pygame.draw.rect(fenetrevoyage,color_bred,[512,550,120,49])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[512,550,120,49])
        if letransport == 2:
            pygame.draw.rect(fenetrevoyage,color_bred,[680,550,190,52])
        else:
            pygame.draw.rect(fenetrevoyage,color_dred,[680,550,190,52])
        fenetrevoyage.blit(taxis , (525,550))
        fenetrevoyage.blit(chauffeur , (695,550))

        # Boutons annuler ou valider
        if 300 <= mouse[0] <= 200+300 and 660 <= mouse[1] <= 75+660:
            pygame.draw.rect(fenetrevoyage,color_crimson,[300,660,200,75])
        else:
            pygame.draw.rect(fenetrevoyage,color_bred,[300,660,200,75])
        fenetrevoyage.blit(annuler , (329,665))
        if 700 <= mouse[0] <= 200+700 and 660 <= mouse[1] <= 75+660:
            pygame.draw.rect(fenetrevoyage,color_spring,[700,660,200,75])
        else:
            pygame.draw.rect(fenetrevoyage,color_sea,[700,660,200,75])
        fenetrevoyage.blit(valider , (733,665))

        #Afficher le message d'erreur
        if erreuroptions > 0:
            fenetrevoyage.blit(choixmanquant , (200,745))

        # Détection d'événements
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            # Vérifie si la souris est cliquée
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Annule la réservation du voyage
                if 300 <= mouse[0] <= 200+300 and 660 <= mouse[1] <= 75+660:
                    principal(sexe,perso,nom,age,argent,salaire,nomlycee,spe,metier,choixdomicile,choixtransport,choixanimaux)
                # Stocker l'option de la classe
                if 357 <= mouse[0] <= 178+357 and 150 <= mouse[1] <= 50+150:
                    laclasse=1
                if 593 <= mouse[0] <= 170+593 and 150 <= mouse[1] <= 50+150:
                    laclasse=2
                if 820 <= mouse[0] <= 175+820 and 150 <= mouse[1] <= 50+150:
                    laclasse=3
                # Stocker l'option de la durée
                if 340 <= mouse[0] <= 60+340 and 254 <= mouse[1] <= 50+254:
                    laduree=1
                if 440 <= mouse[0] <= 60+440 and 254 <= mouse[1] <= 50+254:
                    laduree=2
                if 539 <= mouse[0] <= 60+539 and 254 <= mouse[1] <= 50+254:
                    laduree=3
                if 638 <= mouse[0] <= 60+638 and 254 <= mouse[1] <= 50+254:
                    laduree=4
                if 737 <= mouse[0] <= 60+737 and 254 <= mouse[1] <= 50+254:
                    laduree=5
                if 838 <= mouse[0] <= 60+838 and 254 <= mouse[1] <= 50+254:
                    laduree=6
                if 942 <= mouse[0] <= 65+942 and 254 <= mouse[1] <= 50+254:
                    laduree=7
                # Stocker l'option de la nourriture
                if 440 <= mouse[0] <= 270+440 and 351 <= mouse[1] <= 53+351:
                    lanourriture=1
                if 775 <= mouse[0] <= 220+775 and 351 <= mouse[1] <= 53+351:
                    lanourriture=2
                # Stocker l'option du nombre d'activités
                if 460 <= mouse[0] <= 50+460 and 450 <= mouse[1] <= 50+450:
                    lactivite=1
                if 560 <= mouse[0] <= 50+560 and 450 <= mouse[1] <= 50+450:
                    lactivite=2
                if 660 <= mouse[0] <= 50+660 and 450 <= mouse[1] <= 50+450:
                    lactivite=3
                if 760 <= mouse[0] <= 50+760 and 450 <= mouse[1] <= 50+450:
                    lactivite=4
                if 867 <= mouse[0] <= 50+867 and 450 <= mouse[1] <= 53+450:
                    lactivite=5
                # Stocker l'option du transport
                if 512 <= mouse[0] <= 120+512 and 550 <= mouse[1] <= 49+550:
                    letransport=1
                if 680 <= mouse[0] <= 190+680 and 550 <= mouse[1] <= 52+550:
                    letransport=2
                #Valider
                if 700 <= mouse[0] <= 200+700 and 660 <= mouse[1] <= 75+660:
                    # Affiche un message d'erreur si une des options n'est pas selectionnée
                    if laclasse==0 or laduree==0 or lanourriture==0 or lactivite==0 or letransport==0:
                        erreuroptions=1
                    else:
                        # Variable pour la boucle du compte rendu
                        compterendu=True

                        # Boucle pour faire tourner la page des options du voyage
                        while compterendu:
                            # Mise en place de l'affichage de la fenêtre
                            pygame.display.update()
                            fenetrevoyage = pygame.display.set_mode((width,height))
                            fenetrevoyage.fill(background_colour)
                            # Détection de la position de la souris
                            mouse = pygame.mouse.get_pos()

                            # Calcul du montant du voyage selon les options choisies
                            voyageprix=(int(contenuvoyage[pays][1+laclasse]))+(int(contenuvoyage[pays][4+laduree])*int(contenuvoyage[pays][11+lanourriture]))+(int(contenuvoyage[pays][13+lactivite]))+(int(contenuvoyage[pays][4+laduree])*int(contenuvoyage[pays][18+letransport]))+(int(contenuvoyage[pays][4+laduree])*int(contenuvoyage[pays][21]))

                            # Création des textes pour la page
                            afficherprixvoyage1 = bigfont2.render("Compte Rendu :" , True , color2) # Création du texte
                            afficherprixvoyage01 = mediumfont.render("Destination : "+str(contenuvoyage[pays][0]) , True , color2) # Création du texte
                            afficherprixvoyage2 = mediumfont.render("Classe : " + optionsvoyage[1+laclasse], True , color2) # Création du texte
                            afficherprixvoyage3 = mediumfont.render("Durée : " + optionsvoyage[4+laduree], True , color2) # Création du texte
                            afficherprixvoyage4 = mediumfont.render("Nourriture : " + optionsvoyage[11+lanourriture], True , color2) # Création du texte
                            afficherprixvoyage5 = mediumfont.render("Activités : " + optionsvoyage[13+lactivite], True , color2) # Création du texte
                            afficherprixvoyage6 = mediumfont.render("Transport : " + optionsvoyage[18+letransport], True , color2) # Création du texte
                            afficherprixvoyage7 = smallfont.render("Prix Hôtel : "+ str(contenuvoyage[pays][4+laduree])+ "x" + str(contenuvoyage[pays][21]), True , color2) # Création du texte
                            afficherprixvoyage8 = smallfont.render("(nb de jours x prix par nuit)" , True , color2) # Création du texte
                            afficherprixvoyage9 = bigfont2.render("Prix :" , True , color2) # Création du texte
                            afficherprixvoyage10 = bigfont2.render(str(voyageprix) + "€" , True , color2) # Création du texte
                            fenetrevoyage.blit(traveling , (600,40)) # Affichage de la photo

                            # Blit des textes sur l'écran
                            fenetrevoyage.blit(afficherprixvoyage1 , (50,20))
                            fenetrevoyage.blit(afficherprixvoyage01 , (50,100))
                            fenetrevoyage.blit(afficherprixvoyage2 , (50,150))
                            fenetrevoyage.blit(afficherprixvoyage3 , (50,200))
                            fenetrevoyage.blit(afficherprixvoyage4 , (50,250))
                            fenetrevoyage.blit(afficherprixvoyage5 , (50,300))
                            fenetrevoyage.blit(afficherprixvoyage6 , (50,350))
                            fenetrevoyage.blit(afficherprixvoyage7 , (50,410))
                            fenetrevoyage.blit(afficherprixvoyage8 , (50,445))
                            fenetrevoyage.blit(afficherprixvoyage9 , (50,500))
                            fenetrevoyage.blit(afficherprixvoyage10 , (50,570))

                            # Boutons annuler ou valider
                            if 300 <= mouse[0] <= 200+300 and 660 <= mouse[1] <= 75+660:
                                pygame.draw.rect(fenetrevoyage,color_crimson,[300,660,200,75])
                            else:
                                pygame.draw.rect(fenetrevoyage,color_bred,[300,660,200,75])
                            fenetrevoyage.blit(annuler , (329,665))
                            if 700 <= mouse[0] <= 200+700 and 660 <= mouse[1] <= 75+660:
                                pygame.draw.rect(fenetrevoyage,color_spring,[700,660,200,75])
                            else:
                                pygame.draw.rect(fenetrevoyage,color_sea,[700,660,200,75])
                            fenetrevoyage.blit(valider , (733,665))

                            #Afficher le message d'erreur
                            if erreurargent == 1:
                                fenetrevoyage.blit(toopoortotravel , (260,745))

                            # Détection d'événements
                            for event in pygame.event.get():   # On parcours la liste de tous les événements reçus
                                # Vérifie si la souris est cliquée
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    # Annule la réservation du voyage
                                    if 300 <= mouse[0] <= 200+300 and 660 <= mouse[1] <= 75+660:
                                        principal(sexe,perso,nom,age,argent,salaire,nomlycee,spe,metier,choixdomicile,choixtransport,choixanimaux)
                                    #Valider
                                    if 700 <= mouse[0] <= 200+700 and 660 <= mouse[1] <= 75+660:
                                        # Affiche un message d'erreur si le joueur n'a pas assez d'argent
                                        if variableargent < voyageprix:
                                            erreurargent=1
                                        else:
                                            variableargent=variableargent-voyageprix # Soustrait le prix du voyage à la somme d'argent
                                            principal(sexe,perso,nom,age,variableargent,salaire,nomlycee,spe,metier,choixdomicile,choixtransport,choixanimaux) # Retour au jeu


## Fonction du sexe
# Débute le jeu en fonction du sexe choisi

# Fonction pour faire tourner la fonction principale du jeu en tant que femme
def principal_femme():
    principal(1,random.choice(imagesfemmes),random.choice(nomsfemmes),0,variableargent,0,choixlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)

# Fonction pour faire tourner la fonction principale du jeu en tant qu'homme
def principal_homme():
    principal(2,random.choice(imageshommes),random.choice(nomshommes),0,variableargent,0,choixlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)

## Fonction principale: au début - spécifications et mise en place d'autres couleurs, de variables et création des textes
def principal(sexe,perso,nom,age,argent,salaire,nomlycee,spe,metier,domicile,transport,animaux):
    #Mise en place de la musique
    pygame.mixer.init()
    pygame.mixer.music.load(song2)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    variableage = age
    variableargent = argent

    # Variable pour contenir le choix de la spécialité et le choix du métier
    choix=spe
    choixmetier=metier

    # Variables pour les erreurs
    erreur = 0
    erreur2 = 0

    #Variable pour les différentes pages et boucles du jeu
    fin = False
    edu=False
    jeu=False
    prop=False
    bien=False
    destination=False
    terminer=False

    # Listes vides pour contenir le choix du domicile, du transport et des animaux de compagnie
    choixdomicile=domicile
    choixtransport=transport
    choixanimal=animaux

    # Variables pour stocker l'affichage du texte pour ensuite le blit
    # Texte de la page principale
    nom1 = smallfont.render('Nom: '+nom , True , color)
    age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
    retourmenu = smallfont.render('Retour' , True , color)
    plus = smallfont.render('+' , True , color)
    annee = smallfont.render('une année' , True , color)
    retour = smallfont.render('retour' , True , color)
    argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
    pasdespe = smallfont.render('Pas de spécialité!' , True , color_dark)
    pasdemet = smallfont.render('Pas de métier!' , True , color_dark)

    # Texte de la page éducation
    education = smallfont.render('Education' , True , color)
    enseignement = bigfont.render('Enseignement' , True , color)
    etudes = bigfont.render('Etudes supérieures' , True , color)
    metier = bigfont.render('Métiers' , True , color)
    jeune = bigfont.render("Vous êtes trop jeune pour aller à l'école!" , True , color)
    revenez = bigfont.render("Revenez quand vous aurez 3 ans!" , True , color)
    nommaternelle = smallfont.render(random.choice(listematernelle) , True , color) # Choix aléatoire du nom de l'établissement
    nomprimaire = smallfont.render(random.choice(listeprimaire) , True , color) # Choix aléatoire du nom de l'établissement
    nomcollege = smallfont.render(random.choice(listecollege) , True , color) # Choix aléatoire du nom de l'établissement
    nomlyceee = smallfont.render(nomlycee , True , color) # Choix aléatoire du nom de l'établissement
    faireunchoix = smallfont.render("Choisissez votre spécialité:" , True , color)
    nomuniversite1 = smallfont.render(listeuniversite[0] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite2 = smallfont.render(listeuniversite[1] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite3 = smallfont.render(listeuniversite[2] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite4 = smallfont.render(listeuniversite[3] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite5 = smallfont.render(listeuniversite[4] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite6 = smallfont.render(listeuniversite[5] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite7 = smallfont.render(listeuniversite[6] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite8 = smallfont.render(listeuniversite[7] , True , color) # Extraction des noms de la liste et création du texte
    nomuniversite9 = smallfont.render(listeuniversite[8] , True , color) # Extraction des noms de la liste et création du texte
    specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color) # Création du texte en fonction de la spécialité qui sera choisie
    minijeu = bigfont2.render("Mini-Jeu" , True , color)
    dixmillepartie1 = smallfont.render('Gagnez' , True , color)
    dixmillepartie2 = smallfont.render('10k' , True , color)
    dixmillepartie3 = smallfont.render('par jeu!' , True , color)

    # Texte de la page propriété
    tropjeune1 = bigfont.render('Il faut être majeur' , True , color)
    tropjeune2 = bigfont.render('pour acheter des articles!' , True , color)
    propriete = smallfont.render('Propriété' , True , color)
    proprietebig = bigfont.render('Propriété' , True , color)
    domicile1 = smallfont.render('Domicile:' , True , color)
    domicile2 = smallfont.render('domicile' , True , color)
    transport1 = smallfont.render('Transport:' , True , color)
    transport2 = smallfont.render('transport' , True , color)
    animal1 = smallfont.render('Animaux:' , True , color)
    animal2 = smallfont.render('animal' , True , color)
    aucun = smallfont.render("Vous n'avez aucun" , True , color)
    acheter = smallfont.render('Acheter un' , True , color)

    # Texte de la page bien-être
    bienetre = smallfont.render('Bien-être' , True , color)
    tropjeune3 = bigfont.render('Il faut avoir 16 ans' , True , color)
    tropjeune4 = bigfont.render('pour voyager!' , True , color)
    ladestination = mediumfont.render('Choisir sa:' , True , color2)
    destination = smallfont.render('Destination' , True , color)
    destinationbig = bigfont.render('Voyage' , True , color)
    cliquezdrapeau = smallfont.render('Cliquez sur le drapeau du pays de votre choix...' , True , color_dark)
    envolezvous = smallfont.render('... et envolez vous vers des vacances de rêve!' , True , color_dark)


## Boucle infinie qui fait tourner le jeu

    while not fin:
        # Mise en place de l'affichage de la fenêtre principale
        fenetre.fill(background_colour)
        pygame.draw.rect(fenetre, (255,204,204), pygame.Rect(50, 50, width-100, height-100))
        fenetre.blit(iconfond, (500,210))
        fenetre.blit(perso, (20,250))

        # Détection de la position de la souris
        mouse = pygame.mouse.get_pos()

        # Détection d'événements
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                fin = True      #On arrête la boucle
                pygame.display.quit() #On ferme le display

            # Vérifie si la souris est cliquée
            if event.type == pygame.MOUSEBUTTONDOWN:


## Page éducation

                # Ouverture page éducation
                if 900 <= mouse[0] <= 900+200 and 300 <= mouse[1] <= 300+50:
                    # Variable edu pour ouvrir et fermer la page éducation
                    edu=True
                    # Variables qui contiennent le nom des options en fonction de la spécialité
                    # Création des textes avec le nom du choix de spécialité et du choix de métier
                    nomduchoix = smallfont.render(choix , True , color)
                    nomdumetier = smallfont.render(choixmetier , True , color)
                    nomdumetier2 = mediumfont.render(choixmetier , True , color)
                    option1 = ""
                    option2 = ""
                    option3 = ""
                    option4 = ""
                    option5 = ""
                    a=0

                    # Boucle pour la page éducation
                    while edu:
                        pygame.display.update()
                        fenetreedu = pygame.display.set_mode((width,height))
                        fenetreedu.fill(background_colour)
                        mouse = pygame.mouse.get_pos()

                        # Recherche d'évènements
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # Détection de sélection des boutons
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    edu=False
                                # Sélection des boutons de spécialité quand le personnage aura 19 ans
                                # La spécialité choisie sera stocké dans la variable choix puis les textes seront crées avec les variables nomduchoix et specialite
                                if variableage == 19:
                                    if 150 <= mouse[0] <= 150+250 and 350 <= mouse[1] <= 350+60:
                                        choix = listeuniversite[0]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 450 <= mouse[0] <= 450+250 and 350 <= mouse[1] <= 350+60:
                                        choix = listeuniversite[1]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 750 <= mouse[0] <= 750+250 and 350 <= mouse[1] <= 350+60:
                                        choix = listeuniversite[2]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 150 <= mouse[0] <= 150+250 and 500 <= mouse[1] <= 500+60:
                                        choix = listeuniversite[3]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 450 <= mouse[0] <= 450+250 and 500 <= mouse[1] <= 500+60:
                                        choix = listeuniversite[4]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 750 <= mouse[0] <= 750+250 and 500 <= mouse[1] <= 500+60:
                                        choix = listeuniversite[5]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 150 <= mouse[0] <= 150+250 and 650 <= mouse[1] <= 650+60:
                                        choix = listeuniversite[6]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 450 <= mouse[0] <= 450+250 and 650 <= mouse[1] <= 650+60:
                                        choix = listeuniversite[7]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                    if 750 <= mouse[0] <= 750+250 and 650 <= mouse[1] <= 650+60:
                                        choix = listeuniversite[8]
                                        nomduchoix = smallfont.render(choix , True , color)
                                        specialite = smallfont.render("Spécialité:"+"  "+ choix , True , color)
                                # Sélection des boutons du métier quand le personnage aura 19 ans
                                # Le métier choisi sera stocké dans la variable choixdumetier et le texte sera crée avec la variable nomdumetier
                                if variableage == 24:
                                    if 710 <= mouse[0] <= 710+30 and 262 <= mouse[1] <= 262+30:
                                        choixmetier = option01
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                        nomdumetier2 = mediumfont.render(choixmetier , True , color)
                                        salaire = option001
                                    if 710 <= mouse[0] <= 710+30 and 362 <= mouse[1] <= 362+30:
                                        choixmetier = option02
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                        nomdumetier2 = mediumfont.render(choixmetier , True , color)
                                        salaire = option002
                                    if 710 <= mouse[0] <= 710+30 and 462 <= mouse[1] <= 462+30:
                                        choixmetier = option03
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                        nomdumetier2 = mediumfont.render(choixmetier , True , color)
                                        salaire = option003
                                    if 710 <= mouse[0] <= 710+30 and 562 <= mouse[1] <= 562+30:
                                        choixmetier = option04
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                        nomdumetier2 = mediumfont.render(choixmetier , True , color)
                                        salaire = option004
                                    if 710 <= mouse[0] <= 710+30 and 662 <= mouse[1] <= 662+30:
                                        choixmetier = option05
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                        nomdumetier2 = mediumfont.render(choixmetier , True , color)
                                        salaire = option005

                                # Option pour jouer au mini-jeu
                                if variableage > 24:
                                    if 400 <= mouse[0] <= 400+400 and 430 <= mouse[1] <= 430+200:
                                        jeu=True
                                        while jeu:
                                            # création de la fenêtre
                                            pygame.display.update()
                                            fenetrejeu = pygame.display.set_mode((width,height))

                                            # charger le game
                                            game = Game()

                                            # Variable détection de fin
                                            game.enroute=True
                                            game.gain=False

                                            # variable pour faire tourner le jeu
                                            running= True

                                            #boucle tant que cette condition est vrai
                                            while running:
                                                mouse = pygame.mouse.get_pos()
                                                # appliquer l'arriere plan
                                                fenetrejeu.blit(background, (0, 0))
                                                # Bouton retour à la page principale
                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.draw.rect(fenetrejeu,color_light,[50,50,125,50])
                                                else:
                                                    pygame.draw.rect(fenetrejeu,color_dark,[50,50,125,50])
                                                fenetrejeu.blit(retour , (60,50))
                                                #Commencer le jeu
                                                if game.enroute:
                                                    #déclencher les instruction de la partie
                                                    game.update(fenetrejeu)
                                                elif not game.enroute and game.gain:
                                                    variableargent = variableargent + 10000
                                                    running=False
                                                    jeu=False
                                                else:
                                                    running=False
                                                    jeu=False
                                                # ajouter un son pour le projectile
                                                son = pygame.mixer.Sound('laser.mp3')
                                                # mettre à jour l'ecran
                                                pygame.display.flip()


                                                # Boucle pour les évènements et pour fermer la page
                                                for event in pygame.event.get():
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                            pygame.display.update()
                                                            jeu=False
                                                            running= False

                                                    #detecter si on lache une touche du clavier
                                                    elif event.type == pygame.KEYDOWN:
                                                        game.pressed[event.key]= True
                                                        #detecter si la touche espace est enclenchée pour lancer un projectile
                                                        if event.key == pygame.K_SPACE and game.tirer.full_barre_p():
                                                            game.tirer.pourcentage=0
                                                            game.vaisseau.lancer_projectile()
                                                            son.play()

                                                    elif event.type == pygame.KEYUP:
                                                        game.pressed[event.key]= False


                        # Bouton retour à la page principale
                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                            pygame.draw.rect(fenetreedu,color_light,[50,50,125,50])
                        else:
                            pygame.draw.rect(fenetreedu,color_dark,[50,50,125,50])
                        fenetreedu.blit(retour , (60,50))

                        # Titre de la page éducation qui varie en fonction de l'age
                        if  variableage > 2:
                            pygame.draw.rect(fenetreedu,color_dark,[230,25,900,100])
                        if 2 < variableage <= 18:
                            fenetreedu.blit(enseignement , (510,40))
                        elif 18 < variableage <= 23:
                            fenetreedu.blit(etudes , (460,40))
                        elif variableage > 23:
                            fenetreedu.blit(metier , (590,40))

                        # Rectangle pour embellir la page
                        pygame.draw.rect(fenetreedu,color_dark,[50,165,1080,600])

                        # Retourne un message si le personnage est trop jeune pour commencer son apprentissage
                        if variableage < 3:
                            fenetreedu.blit(jeune , (100,350))
                            fenetreedu.blit(revenez , (200,450))

                        # Nom de l'établissement en fonction de l'age
                        # Maternelle
                        if 2 < variableage < 7:
                            fenetreedu.blit(nommaternelle , (150,185))
                            fenetreedu.blit(maternelle , (125,260))
                        # Primaire
                        if 6 < variableage < 12:
                            fenetreedu.blit(nomprimaire , (150,185))
                            fenetreedu.blit(primaire , (125,260))
                        # Collège
                        if 11 < variableage < 16:
                            fenetreedu.blit(nomcollege , (150,185))
                            fenetreedu.blit(college , (125,260))
                        # Lycée
                        if 15 < variableage < 19:
                            fenetreedu.blit(nomlyceee , (150,185))
                            fenetreedu.blit(lycee , (125,260))

                        # Mise en place des rectangles des boutons qui changent de couleurs si la souris est au-dessus
                        if variableage == 19:
                            if 150 <= mouse[0] <= 150+250 and 350 <= mouse[1] <= 350+60:
                                pygame.draw.rect(fenetreedu,color_bred,[150,350,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[150,350,250,60])
                            if 450 <= mouse[0] <= 450+250 and 350 <= mouse[1] <= 350+60:
                                pygame.draw.rect(fenetreedu,color_bred,[450,350,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[450,350,250,60])
                            if 750 <= mouse[0] <= 750+250 and 350 <= mouse[1] <= 350+60:
                                pygame.draw.rect(fenetreedu,color_bred,[750,350,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[750,350,250,60])
                            if 150 <= mouse[0] <= 150+250 and 500 <= mouse[1] <= 500+60:
                                pygame.draw.rect(fenetreedu,color_bred,[150,500,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[150,500,250,60])
                            if 450 <= mouse[0] <= 450+250 and 500 <= mouse[1] <= 500+60:
                                pygame.draw.rect(fenetreedu,color_bred,[450,500,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[450,500,250,60])
                            if 750 <= mouse[0] <= 750+250 and 500 <= mouse[1] <= 500+60:
                                pygame.draw.rect(fenetreedu,color_bred,[750,500,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[750,500,250,60])
                            if 150 <= mouse[0] <= 150+250 and 650 <= mouse[1] <= 650+60:
                                pygame.draw.rect(fenetreedu,color_bred,[150,650,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[150,650,250,60])
                            if 450 <= mouse[0] <= 450+250 and 650 <= mouse[1] <= 650+60:
                                pygame.draw.rect(fenetreedu,color_bred,[450,650,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[450,650,250,60])
                            if 750 <= mouse[0] <= 750+250 and 650 <= mouse[1] <= 650+60:
                                pygame.draw.rect(fenetreedu,color_bred,[750,650,250,60])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[750,650,250,60])

                            # Affichage du texte faire un choix
                            fenetreedu.blit(faireunchoix , (250,225))

                            # Superposition des noms de spécialité sur les boutons
                            fenetreedu.blit(nomuniversite1 , (192,355))
                            fenetreedu.blit(nomuniversite2 , (500,355))
                            fenetreedu.blit(nomuniversite3 , (815,355))
                            fenetreedu.blit(nomuniversite4 , (230,505))
                            fenetreedu.blit(nomuniversite5 , (510,505))
                            fenetreedu.blit(nomuniversite6 , (785,505))
                            fenetreedu.blit(nomuniversite7 , (230,655))
                            fenetreedu.blit(nomuniversite8 , (468,655))
                            fenetreedu.blit(nomuniversite9 , (795,655))

                            # Affichage du nom du choix de spécialité
                            fenetreedu.blit(nomduchoix , (725,225))

                        # Affichage de la spécialité choisie pendant les 5 ans d'université
                        if variableage > 19 and variableage <= 23:
                            fenetreedu.blit(specialite , (100,175))
                            fenetreedu.blit(school , (100,235))

                        # Code pour le fonctionnement du choix des métiers
                        if variableage == 24:
                            # Détection du choix de spécialité fait avant et créations des 5 options
                            # In range 9 car il y a 9 spés
                            for i in range (9):
                                # Code mathématique pour déterminer et calculer les options en fonctions de la spécialité
                                if choix == listeuniversite[i]:
                                    a=i*5
                                    option1 = smallfont.render(dicometiers[a][0] , True , color)
                                    option01 = dicometiers[a][0]
                                    option001 = dicometiers[a][1]
                                    option2 = smallfont.render(dicometiers[a+1][0] , True , color)
                                    option02 = dicometiers[a+1][0]
                                    option002 = dicometiers[a+1][1]
                                    option3 = smallfont.render(dicometiers[a+2][0] , True , color)
                                    option03 = dicometiers[a+2][0]
                                    option003 = dicometiers[a+2][1]
                                    option4 = smallfont.render(dicometiers[a+3][0] , True , color)
                                    option04 = dicometiers[a+3][0]
                                    option004 = dicometiers[a+3][1]
                                    option5 = smallfont.render(dicometiers[a+4][0] , True , color)
                                    option05 = dicometiers[a+4][0]
                                    option005 = dicometiers[a+4][1]

                            # Affichage des textes des choix de métiers
                            fenetreedu.blit(option1 , (800,250))
                            fenetreedu.blit(option2 , (800,350))
                            fenetreedu.blit(option3 , (800,450))
                            fenetreedu.blit(option4 , (800,550))
                            fenetreedu.blit(option5 , (800,650))

                            # Affichage du choix selectionné
                            fenetreedu.blit(nomdumetier , (270,250))

                            # Affichage de l'image de l'interview
                            fenetreedu.blit(interview, (70,330))

                            # Mise en place des rectangles des boutons qui changent de couleurs si la souris est au-dessus
                            if 710 <= mouse[0] <= 710+30 and 262 <= mouse[1] <= 262+30:
                                pygame.draw.rect(fenetreedu,color_dred,[710,262,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_bred,[710,262,30,30])
                            if 710 <= mouse[0] <= 710+30 and 362 <= mouse[1] <= 362+30:
                                pygame.draw.rect(fenetreedu,color_dred,[710,362,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_bred,[710,362,30,30])
                            if 710 <= mouse[0] <= 710+30 and 462 <= mouse[1] <= 462+30:
                                pygame.draw.rect(fenetreedu,color_dred,[710,462,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_bred,[710,462,30,30])
                            if 710 <= mouse[0] <= 710+30 and 562 <= mouse[1] <= 562+30:
                                pygame.draw.rect(fenetreedu,color_dred,[710,562,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_bred,[710,562,30,30])
                            if 710 <= mouse[0] <= 710+30 and 662 <= mouse[1] <= 662+30:
                                pygame.draw.rect(fenetreedu,color_dred,[710,662,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_bred,[710,662,30,30])

                        # Affichage du métier choisis après les études
                        if variableage > 24:
                            fenetreedu.blit(bannermiddle , (358,170))
                            fenetreedu.blit(nomdumetier2 , (450,250))
                            if 390 <= mouse[0] <= 390+400 and 430 <= mouse[1] <= 430+200:
                                pygame.draw.rect(fenetreedu,game_colour1,[390,430,400,200])
                            else:
                                pygame.draw.rect(fenetreedu,game_colour2,[390,430,400,200])
                            fenetreedu.blit(minijeu,(467,477))
                            fenetreedu.blit(bannerleft , (-20,170))
                            fenetreedu.blit(bannerright , (800,170))
                            fenetreedu.blit(dixmillepartie1 , (155,375))
                            fenetreedu.blit(dixmillepartie2 , (185,425))
                            fenetreedu.blit(dixmillepartie3 , (155,475))
                            fenetreedu.blit(dixmillepartie1 , (910,375))
                            fenetreedu.blit(dixmillepartie2 , (940,425))
                            fenetreedu.blit(dixmillepartie3 , (910,475))


## Page propriété

                # Ouverture de la page propriété
                if 900 <= mouse[0] <= 900+200 and 400 <= mouse[1] <= 400+50:
                    # Variable prop pour ouvrir et fermer la page propriété
                    prop=True
                    # Boucle pour la page propriété
                    while prop:
                        pygame.display.update()
                        fenetreprop = pygame.display.set_mode((width,height))
                        fenetreprop.fill(background_colour)
                        mouse = pygame.mouse.get_pos()

                        # Bouton retour à la page principale
                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                            pygame.draw.rect(fenetreprop,color_light,[50,50,125,50])
                        else:
                            pygame.draw.rect(fenetreprop,color_dark,[50,50,125,50])
                        fenetreprop.blit(retour , (60,50))

                        # Titre de la page
                        pygame.draw.rect(fenetreprop,color_dark,[230,25,900,100])
                        fenetreprop.blit(proprietebig , (580,40))

                        # Eléments de la page
                        # Rectangles pour le décor
                        pygame.draw.rect(fenetreprop,color_dark,[50,165,1080,600])

                        if variableage < 18:
                            fenetreprop.blit(tropjeune1 , (360,350))
                            fenetreprop.blit(tropjeune2 , (290,450))
                        elif variableage > 17:
                            pygame.draw.rect(fenetreprop,color_red,[80,190,326,550])
                            pygame.draw.rect(fenetreprop,color_red,[427,190,326,550])
                            pygame.draw.rect(fenetreprop,color_red,[774,190,326,550])

                            # Affichage des noms des catégories
                            fenetreprop.blit(domicile1 , (160,200))
                            fenetreprop.blit(transport1 , (500,200))
                            fenetreprop.blit(animal1 , (860,200))

                            # Contenu des catégories
                            # Domicile
                            if choixdomicile==[]:
                                fenetreprop.blit(aucun , (95,400))
                                fenetreprop.blit(domicile2 , (170,450))
                            else:
                                b=265
                                for i in range (len(choixdomicile)):
                                    optiondom = smallfont.render(choixdomicile[i] , True , color)
                                    fenetreprop.blit(optiondom , (100,b))
                                    b=b+50

                            if 100 <= mouse[0] <= 100+286 and 625 <= mouse[1] <= 625+100:
                                pygame.draw.rect(fenetreprop,color_dred,[100,625,286,100])
                            else:
                                pygame.draw.rect(fenetreprop,color_bred,[100,625,286,100])
                            fenetreprop.blit(acheter , (150,625))
                            fenetreprop.blit(domicile2 , (170,675))

                            # Transport
                            if choixtransport==[]:
                                fenetreprop.blit(aucun , (445,400))
                                fenetreprop.blit(transport2 , (510,450))
                            else:
                                c=265
                                for i in range (len(choixtransport)):
                                    optiontra = smallfont.render(choixtransport[i] , True , color)
                                    fenetreprop.blit(optiontra , (447,c))
                                    c=c+50
                            if 447 <= mouse[0] <= 447+286 and 650 <= mouse[1] <= 650+100:
                                pygame.draw.rect(fenetreprop,color_dred,[447,625,286,100])
                            else:
                                pygame.draw.rect(fenetreprop,color_bred,[447,625,286,100])
                            fenetreprop.blit(acheter , (500,625))
                            fenetreprop.blit(transport2 , (510,675))

                            # Animal
                            if choixanimal==[]:
                                fenetreprop.blit(aucun , (790,400))
                                fenetreprop.blit(animal2 , (880,450))
                            else:
                                d=265
                                for i in range (len(choixanimal)):
                                    optionani = smallfont.render(choixanimal[i] , True , color)
                                    fenetreprop.blit(optionani , (794,d))
                                    d=d+50
                            if 794 <= mouse[0] <= 794+286 and 650 <= mouse[1] <= 650+100:
                                pygame.draw.rect(fenetreprop,color_dred,[794,625,286,100])
                            else:
                                pygame.draw.rect(fenetreprop,color_bred,[794,625,286,100])
                            fenetreprop.blit(acheter , (840,625))
                            fenetreprop.blit(animal2 , (880,675))

                        # Boucle pour les évènements et pour fermer la page
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    prop=False

                                #domicile
                                if 100 <= mouse[0] <= 100+286 and 625 <= mouse[1] <= 625+100:
                                    lemagasin(1,listedomicile,choixdomicile,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                #transport
                                if 447 <= mouse[0] <= 447+286 and 625 <= mouse[1] <= 625+100:
                                    lemagasin(2,listetransport,choixtransport,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)

                                #animal
                                if 794 <= mouse[0] <= 794+286 and 625 <= mouse[1] <= 625+100:
                                    lemagasin(3,listeanimal,choixanimal,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)


## Page bien-être

                # Ouverture de la page bien-être
                if 900 <= mouse[0] <= 900+200 and 500 <= mouse[1] <= 500+50:
                    # Variable bien pour ouvrir et fermer la page bien-être
                    bien=True
                    # Boucle pour la page bien-être
                    while bien:
                        # création de la fenêtre
                        pygame.display.update()
                        fenetrebien = pygame.display.set_mode((width,height))
                        fenetrebien.fill(background_colour)
                        mouse = pygame.mouse.get_pos()

                        #Voyager en fonction de l'age
                        if variableage < 16:
                            # Titre de la page
                            pygame.draw.rect(fenetrebien,color_dark,[230,25,900,100])
                            fenetrebien.blit(destinationbig , (580,40))
                            pygame.draw.rect(fenetrebien,color_dark,[50,165,1080,600])
                            fenetrebien.blit(tropjeune3 , (375,350))
                            fenetrebien.blit(tropjeune4 , (440,450))
                        elif variableage > 15:
                            # Bouton destination
                            fenetrebien.blit(fondbienetre , (25,25))
                            if 500 <= mouse[0] <= 250+500 and 425 <= mouse[1] <= 100+425:
                                pygame.draw.rect(fenetrebien,color_navy,[500,425,250,100])
                            else:
                                pygame.draw.rect(fenetrebien,color_blue,[500,425,250,100])
                            fenetrebien.blit(ladestination , (530,350))
                            fenetrebien.blit(destination , (532,450))

                        # Bouton retour à la page principale
                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                            pygame.draw.rect(fenetrebien,color_light,[50,50,125,50])
                        else:
                            pygame.draw.rect(fenetrebien,color_dark,[50,50,125,50])
                        fenetrebien.blit(retour , (60,50))

                        # Boucle pour les évènements et pour fermer la page
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    bien=False
                                if 500 <= mouse[0] <= 250+500 and 425 <= mouse[1] <= 100+425:
                                    destination=True
                                    while destination:
                                        pygame.display.update()
                                        fenetrebien = pygame.display.set_mode((width,height))
                                        fenetrebien.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()
                                        fenetrebien.blit(cliquezdrapeau , (220,35))
                                        fenetrebien.blit(france , (50,115))
                                        fenetrebien.blit(espagne , (275,115))
                                        fenetrebien.blit(etatsunis , (500,115))
                                        fenetrebien.blit(italie , (725,115))
                                        fenetrebien.blit(mexique , (950,115))
                                        fenetrebien.blit(allemagne , (50,265))
                                        fenetrebien.blit(thailande , (275,265))
                                        fenetrebien.blit(nouvellezelande , (500,265))
                                        fenetrebien.blit(angleterre , (725,265))
                                        fenetrebien.blit(japon , (950,265))
                                        fenetrebien.blit(grece , (50,415))
                                        fenetrebien.blit(chine , (275,415))
                                        fenetrebien.blit(malaisie , (500,415))
                                        fenetrebien.blit(russie , (725,415))
                                        fenetrebien.blit(portugal , (950,415))
                                        fenetrebien.blit(canada , (50,565))
                                        fenetrebien.blit(pologne , (275,565))
                                        fenetrebien.blit(paysbas , (500,565))
                                        fenetrebien.blit(australia , (725,565))
                                        fenetrebien.blit(austria , (950,565))
                                        fenetrebien.blit(envolezvous , (240,715))

                                        # Boucle pour les évènements et pour fermer la page
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                #1
                                                if 50 <= mouse[0] <= 200+50 and 115 <= mouse[1] <= 120+115:
                                                    levoyage(0,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #2
                                                if 275 <= mouse[0] <= 200+275 and 115 <= mouse[1] <= 120+115:
                                                    levoyage(1,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #3
                                                if 500 <= mouse[0] <= 200+500 and 115 <= mouse[1] <= 120+115:
                                                    levoyage(2,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #4
                                                if 725 <= mouse[0] <= 200+725 and 115 <= mouse[1] <= 120+115:
                                                    levoyage(3,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #5
                                                if 950 <= mouse[0] <= 200+950 and 115 <= mouse[1] <= 120+115:
                                                    levoyage(4,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #6
                                                if 50 <= mouse[0] <= 200+50 and 265 <= mouse[1] <= 120+265:
                                                    levoyage(5,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #7
                                                if 275 <= mouse[0] <= 200+275 and 265 <= mouse[1] <= 120+265:
                                                    levoyage(6,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #8
                                                if 500 <= mouse[0] <= 200+500 and 265 <= mouse[1] <= 120+265:
                                                    levoyage(7,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #9
                                                if 725 <= mouse[0] <= 200+725 and 265 <= mouse[1] <= 120+265:
                                                    levoyage(8,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #10
                                                if 950 <= mouse[0] <= 200+950 and 265 <= mouse[1] <= 120+265:
                                                    levoyage(9,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #11
                                                if 50 <= mouse[0] <= 200+50 and 415 <= mouse[1] <= 120+415:
                                                    levoyage(10,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #12
                                                if 275 <= mouse[0] <= 200+275 and 415 <= mouse[1] <= 120+415:
                                                    levoyage(11,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #13
                                                if 500 <= mouse[0] <= 200+500 and 415 <= mouse[1] <= 120+415:
                                                    levoyage(12,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #14
                                                if 725 <= mouse[0] <= 200+725 and 415 <= mouse[1] <= 120+415:
                                                    levoyage(13,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #15
                                                if 950 <= mouse[0] <= 200+950 and 415 <= mouse[1] <= 120+415:
                                                    levoyage(14,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #16
                                                if 50 <= mouse[0] <= 200+50 and 565 <= mouse[1] <= 120+565:
                                                    levoyage(15,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #17
                                                if 275 <= mouse[0] <= 200+275 and 565 <= mouse[1] <= 120+565:
                                                    levoyage(16,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #18
                                                if 500 <= mouse[0] <= 200+500 and 565 <= mouse[1] <= 120+565:
                                                    levoyage(17,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #19
                                                if 725 <= mouse[0] <= 200+725 and 565 <= mouse[1] <= 120+565:
                                                    levoyage(18,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)
                                                #20
                                                if 950 <= mouse[0] <= 200+950 and 565 <= mouse[1] <= 120+565:
                                                    levoyage(19,sexe,perso,nom,variableage,variableargent,salaire,nomlycee,choix,choixmetier,choixdomicile,choixtransport,choixanimal)


## Bouton age

                # Variation de l'age si le bouton + une année est cliqué
                if 525 <= mouse[0] <= 525+200 and 510 <= mouse[1] <= 510+100:
                    # Le joueur peut avancer d'un an s'il à moins de 100 ans
                    if variableage < 100:
                        # Ajout du salaire annuel après avoir un métier
                        if variableage > 24:
                            variableargent = variableargent + (salaire*12)
                            # Arrondi le montant pour ne pas depasser du rectangle sur l'interface
                            if 9999 < variableargent < 1000000:
                                arrondi = round(variableargent/1000, 1)
                                argent = bigfont.render(str(arrondi)+" K "+'€', True , color)
                            elif 999999 < variableargent:
                                arrondi = round(variableargent/1000000, 2)
                                argent = bigfont.render(str(arrondi)+" M "+'€', True , color)
                            else:
                                argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
                            fenetre.blit(argent , (865,125))
                        # Si tout est bon, la variable variableage s'incrémente de 1 et le texte de l'age est rafraichît
                        if variableage != 19 and variableage != 24:
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                        # Il ne peut pas avancer d'un an s'il n'a pas choisi de spécialité à 19 ans
                        elif variableage == 19 and choix == "":
                            erreur = erreur+1
                        # Si une spécialité est choisie il peut avancer
                        elif variableage == 19 and choix != "":
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                        # Il ne peut pas avancer d'un an s'il n'a pas choisi de métier à 24 ans
                        elif variableage == 24 and choixmetier == "":
                            erreur2 = erreur2+1
                        # Si un métier est choisi il peut avancer et recevra son premier salaire
                        elif variableage == 24 and choixmetier != "":
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                            variableargent = variableargent + (salaire*12)
                            # Arrondir le montant pour ne pas depasser du rectangle sur l'interface
                            if 9999 < variableargent < 1000000:
                                arrondi = round(variableargent/1000, 1)
                                argent = bigfont.render(str(arrondi)+" K "+'€', True , color)
                            elif 999999 < variableargent:
                                arrondi = round(variableargent/1000000, 2)
                                argent = bigfont.render(str(arrondi)+" M "+'€', True , color)
                            else:
                                argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
                            fenetre.blit(argent , (865,125))


                    # Si la personne est arrivée à 100 ans, le jeu se termine
                    else:
                        terminer= True


                    # Affichage de l'écran de fin
                    while terminer:
                        pygame.display.update()
                        fenetretermine = pygame.display.set_mode((width,height))
                        fenetretermine.fill(background_colour)
                        mouse = pygame.mouse.get_pos()
                        # Texte de terminer
                        termine = bigfont.render("Vous avez atteint 100 ans, le jeu est terminé!" , True , color)
                        nomtermine = smallfont.render('Nom: '+ nom , True , color)
                        agetermine = smallfont.render('Age : '+str(variableage), True , color)
                        domicile3 = smallfont.render('Domicile :' , True , color)
                        transport3 = smallfont.render('Transport :' , True , color)
                        animal3 = smallfont.render('Animal :' , True , color)
                        if 9999 < variableargent < 1000000:
                            arrondi = round(variableargent/1000, 1)
                            argenttermine2 = str(arrondi)+" K "+"€"
                        elif 999999 < variableargent:
                            arrondi = round(variableargent/1000000, 2)
                            argenttermine2 = str(arrondi)+" M "+"€"
                        else:
                            argenttermine2 = str(variableargent)+" "+"€"
                        argenttermine = smallfont.render('Argent : '+argenttermine2, True , color)
                        # Affichage du texte de fin
                        fenetretermine.blit(termine , (60,50))
                        fenetretermine.blit(nomtermine , (60,150))
                        fenetretermine.blit(agetermine , (60,200))
                        fenetretermine.blit(argenttermine , (60,250))

                        # Domicile
                        if choixdomicile==[]:
                            fenetretermine.blit(aucun , (60,350))
                            fenetretermine.blit(domicile2 , (360,350))
                        else:
                            fenetretermine.blit(domicile3 , (60,325))
                            b=310
                            bb=325
                            for i in range (len(choixdomicile)):
                                if i < 3:
                                    optiondom = smallfont.render(choixdomicile[i] , True , color)
                                    fenetretermine.blit(optiondom , (b,bb))
                                if i > 2:
                                    optiondom = smallfont.render(choixdomicile[i] , True , color)
                                    fenetretermine.blit(optiondom , (b-1000,bb+50))
                                b=b+250

                        # Transport
                        if choixtransport==[]:
                            fenetretermine.blit(aucun , (60,475))
                            fenetretermine.blit(transport2 , (360,475))
                        else:
                            fenetretermine.blit(transport3 , (60,450))
                            c=310
                            cc=450
                            for i in range (len(choixtransport)):
                                if i < 3:
                                    optiontra = smallfont.render(choixtransport[i] , True , color)
                                    fenetretermine.blit(optiontra , (c,cc))
                                if i > 2:
                                    optiontra = smallfont.render(choixtransport[i] , True , color)
                                    fenetretermine.blit(optiontra , (c-1000,cc+50))
                                c=c+250

                        # Animal
                        if choixanimal==[]:
                            fenetretermine.blit(aucun , (60,600))
                            fenetretermine.blit(animal2 , (360,600))
                        else:
                            fenetretermine.blit(animal3 , (60,575))
                            d=310
                            dd=575
                            for i in range (len(choixanimal)):
                                if i < 3:
                                    optionani = smallfont.render(choixanimal[i] , True , color)
                                    fenetretermine.blit(optionani , (d,dd))
                                if i > 2:
                                    optionani = smallfont.render(choixanimal[i] , True , color)
                                    fenetretermine.blit(optionani , (d-1000,dd+50))
                                d=d+250

                        #On parcours la liste de tous les événements reçus
                        for event in pygame.event.get():
                            #Si un de ces événements est de type QUIT on ferme le jeu
                            if event.type == QUIT:
                                terminer = False
                                fin = True
                                pygame.display.quit()


## Bouton retour

                # Bouton retour au menu du départ
                if 900 <= mouse[0] <= 900+200 and 600 <= mouse[1] <= 600+50:
                    sexe=0
                    depart()


## Mise en place des rectangles des boutons de le page pricipale qui changent de couleurs si la souris est au-dessus

        # Bouton éducation
        if 900 <= mouse[0] <= 900+200 and 300 <= mouse[1] <= 300+50:
            pygame.draw.rect(fenetre,color_light,[900,300,200,50])
        else:
            pygame.draw.rect(fenetre,color_dark,[900,300,200,50])

        # Bouton propriété
        if 900 <= mouse[0] <= 900+200 and 400 <= mouse[1] <= 400+50:
            pygame.draw.rect(fenetre,color_light,[900,400,200,50])
        else:
            pygame.draw.rect(fenetre,color_dark,[900,400,200,50])

        # Bouton bien-être
        if 900 <= mouse[0] <= 900+200 and 500 <= mouse[1] <= 500+50:
            pygame.draw.rect(fenetre,color_light,[900,500,200,50])
        else:
            pygame.draw.rect(fenetre,color_dark,[900,500,200,50])

        # Bouton retour
        if 900 <= mouse[0] <= 900+200 and 600 <= mouse[1] <= 600+50:
            pygame.draw.rect(fenetre,color_light,[900,600,200,50])
        else:
            pygame.draw.rect(fenetre,color_dark,[900,600,200,50])

        # Bouton année
        if 525 <= mouse[0] <= 525+200 and 510 <= mouse[1] <= 510+100:
            pygame.draw.rect(fenetre,color_light,[525,510,200,100])
        else:
            pygame.draw.rect(fenetre,color_dark,[525,510,200,100])


## Affichage des éléments de la page principale

        # Affichage de l'identité sur un rectangle par superposition
        pygame.draw.rect(fenetre,color_dark,[80,100,365,100])
        fenetre.blit(nom1 , (85,105))
        fenetre.blit(age , (85,145))

        # Affichage du montant de l'argent
        pygame.draw.rect(fenetre,color_dark,[850,100,250,120])
        if 9999 < variableargent < 1000000:
            arrondi = round(variableargent/1000, 1)
            argent = bigfont.render(str(arrondi)+" K "+'€', True , color)
        elif 999999 < variableargent:
            arrondi = round(variableargent/1000000, 2)
            argent = bigfont.render(str(arrondi)+" M "+'€', True , color)
        else:
            argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
        fenetre.blit(argent , (865,125))

        # Affichage des textes de la page principale sur les boutons par superposition
        fenetre.blit(plus , (615,510))
        fenetre.blit(annee , (546,550))
        fenetre.blit(education , (923,300))
        fenetre.blit(propriete , (925,400))
        fenetre.blit(bienetre , (922,500))
        fenetre.blit(retourmenu , (945,600))

        # Erreurs
        if erreur > 0 and variableage == 19 and choix == "":
            fenetre.blit(pasdespe , (485,640))
        if erreur2 > 0 and variableage == 24 and choixmetier == "":
            fenetre.blit(pasdemet , (510,640))

        # Update le display du jeu
        pygame.display.update()
        pygame.display.flip()


## Faire tourner le jeu
# Initialisation de pygame et de la musique
pygame.init()
pygame.mixer.init()
# Commencer et faire tourner le jeu
depart()
