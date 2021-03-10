#Importation des bibliothèques
import pygame
import pygame_menu
import random
from random import randint
from pygame.locals import *
from game import Game
from player import Vaisseau
from projectile import Projectile
import tkinter
from tkinter import messagebox



# Initialisation de pygame
pygame.init()


## Mise en place de la fenêtre, des listes, des images, des couleurs et une variable

#Création de la fenêtre
width = 1200
height = 800
background_colour = (255,153,153)
fenetre = pygame.display.set_mode((width,height))
fenetre.fill(background_colour)
gamename = pygame.display.set_caption("Onlife")
icon = pygame.image.load('icon.png').convert_alpha()
iconfond =pygame.transform.scale(icon,(250,250))
gameicon = pygame.display.set_icon(icon)


# Listes de noms
nomsfemmes=["Clara Cuoghi","Aurélie Gallet"]
nomshommes=["Rayane Dahmoul","Haroun Abidi"]

# Images
femme1=pygame.image.load('Femme1.png').convert_alpha()
femme2=pygame.image.load('Femme2.png').convert_alpha()
femme3=pygame.image.load('Femme3.png').convert_alpha()
femme4=pygame.image.load('Femme4.png').convert_alpha()

homme1=pygame.image.load('Homme1.png').convert_alpha()
homme2=pygame.image.load('Homme2.png').convert_alpha()
homme3=pygame.image.load('Homme3.png').convert_alpha()
homme4=pygame.image.load('Homme4.png').convert_alpha()
homme5=pygame.image.load('Homme5.png').convert_alpha()

imagesfemmes=[femme1,femme2,femme3,femme4]
imageshommes=[homme1,homme2,homme3,homme4,homme5]


# Theme personalisé pour les menus
mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.background_color=(255,204,204)
mytheme.title_background_color=(255,153,153)
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
mytheme.title_font=pygame_menu.font.FONT_COMIC_NEUE
mytheme.title_font_color=(0,0,0)
mytheme.widget_font=pygame_menu.font.FONT_NEVIS
mytheme.widget_font_color=(0,0,0)

# Variable pour le sexe choisis
sexe = 0

# Variable du salaire (aléatoire pour le moment)
salaire = randint(1200, 3500)

#Listes pour la page enseignement
listematernelle=["Ecole maternelle Béré","Ecole maternelle Le Coudray","Ecole maternelle Henri Bergson","Ecole maternelle Jules Ferry","Ecole maternelle Claude Monet","Ecole maternelle Prince Bois","Ecole maternelle Le Bourgeau","Ecole maternelle du Massif","Ecole maternelle Molière","Ecole maternelle du Centre"]
listeprimaire=["Ecole primaire Guillaume Apollinaire","Ecole primaire Michel Servet","Ecole primaire Albert Barraud","Ecoles primaire les Néréides","Ecole primaire Jean Jaurès","Ecole primaire Jacques Prévert","Ecole primaire Charles Perrault","Ecole primaire La Clé des Champs","Ecole primaire Les Nondales","Ecole primaire L'Arbre Enchanté"]
listecollege=["Collège Chaptal","Collège Plaisance","Collège Jean Giono","Collège les Fontainettes","Collège Victor Hugo","Collège des Trois Vallées","Collège la Sablière","Collège Antoine de Saint-Exupéry","Collège Claude Nicolas le Doux","Collège Les Franchises"]
listelycee=["Lycée Jean Rostand","Lycée Henri Vincenot","Lycée Camille Claudel","Lycée Pasteur","Lycée Gustave Eiffel","Lycée Voltaire","Lycée Parc des Loges","Lycée Martin Luther King","Lycée Honoré Romane","Lycée Jean Monnet"]
listeuniversite=["Commerce","Ingénieur","Lettres","Arts","Politique","Sc.Sociales","Droit","Architecture","Médecine"]
dicometiers=["Commerce1","Commerce2","Commerce3","Commerce4","Commerce5","Ingénieur1","Ingénieur2","Ingénieur3","Ingénieur4","Ingénieur5","Lettres1","Lettres2","Lettres3","Lettres4","Lettres5","Arts1","Arts2","Arts3","Arts4","Arts5","Politique1","Politique2","Politique3","Politique4","Politique5","Sc.Sociales1","Sc.Sociales2","Sc.Sociales3","Sc.Sociales4","Sc.Sociales5","Droit1","Droit2","Droit3","Droit4","Droit5","Architecture1","Architecture2","Architecture3","Architecture4","Architecture5","Médecine1","Médecine2","Médecine3","Médecine4","Médecine5"]
listedomicile=["Studio1","Studio2","Studio3","Studio4","Studio5","Appartement1","Appartement2","Appartement3","Appartement4","Appartement5","Maison1","Maison2","Maison1","Maison2","Maison3","Maison4","Maison5","Villa1","Villa2""Villa3""Villa4""Villa5"]
listetransport=[]
listeanimal=[]


## Fonction menu

# Code pour faire tourner la fonction menu pour choisir le sexe
def sexe():
    pygame.init()
    ecran = pygame_menu.Menu(800, 1200, 'ONLIFE',theme=mytheme)
    genre = ecran.add_image('femmehomme.png')
    femme = ecran.add_button('Femme',principal_femme)
    homme = ecran.add_button('Homme',principal_homme)
    ecran.add_button('Retour',depart)
    ecran.mainloop(fenetre)
    return sexe


## Fonction option

#Fonction option à remplir
def option_the_game():
    return option_the_game


## Fonction du sexe

# Fonction pour faire tourner la fonction principale du jeu en tant que femme
def principal_femme():
    principal(1)

# Fonction pour faire tourner la fonction principale du jeu en tant qu'homme
def principal_homme():
    principal(2)


## Fonction principale: au début - spécifications et mise en place d'autres couleurs, de variables et création des textes

def principal(sexe):
    #Variables de l'age et de l'argent
    variableage = 0
    variableargent = 0

    #Variable pour les différentes pages et boucles du jeu
    fin = False
    edu=False
    prop=False
    bien=False
    terminer=False

    # Variable pour contenir le choix de la spécialité et le choix du métier
    choix=""
    choixmetier=""

    # Listes vides pour contenir le choix du domicile, du transport et des animaux de compagnie
    choixdomicile=[]
    choixtransport=[]
    choixanimal=[]

    # Couleur blanche du texte
    color = (255,255,255)

    # Couleurs pour les différents rectangles de fond
    color_light = (170,170,170)
    color_dark = (100,100,100)
    color_red = (249,113,113)
    color_dred = (220,20,60)
    color_bred = (207,69,96)

    # Police du texte avec deux tailles différentes
    smallfont = pygame.font.SysFont('comicsansms',35)
    bigfont = pygame.font.SysFont('comicsansms',50)

    # Variables pour stocker l'affichage du texte pour ensuite le blit
    # Texte de la page principale
    if sexe == 1:
        nomfemme = smallfont.render('Nom: '+random.choice(nomsfemmes) , True , color)
    elif sexe == 2:
        nomhomme = smallfont.render('Nom: '+random.choice(nomshommes) , True , color)
    age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
    retourmenu = smallfont.render('Retour' , True , color)
    plus = smallfont.render('+' , True , color)
    annee = smallfont.render('une année' , True , color)
    retour = smallfont.render('retour' , True , color)
    argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
    termine = bigfont.render("Vous avez atteint 100 ans, le jeu est terminé!" , True , color)

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
    nomlycee = smallfont.render(random.choice(listelycee) , True , color) # Choix aléatoire du nom de l'établissement
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

    # Texte de la page propriété
    propriete = smallfont.render('Propriété' , True , color)
    proprietebig = bigfont.render('Propriété' , True , color)
    domicile = smallfont.render('Domicile:' , True , color)
    transport = smallfont.render('Transport:' , True , color)
    animal = smallfont.render('Animaux:' , True , color)
    aucun = smallfont.render("Vous n'avez aucun" , True , color)
    domicile1 = smallfont.render('domicile' , True , color)
    transport1 = smallfont.render('transport' , True , color)
    animal1 = smallfont.render('animal' , True , color)
    acheter = smallfont.render('Acheter un' , True , color)

    # Texte de la page bien-être
    bienetre = smallfont.render('Bien-être' , True , color)

    # Image du personnage en fonction du sexe
    if sexe == 1:
        persofemme=random.choice(imagesfemmes)
    elif sexe == 2:
        persohomme=random.choice(imageshommes)


## Boucle infinie qui fait tourner le jeu

    while not fin:
        # Mise en place de l'affichage de la fenêtre principale
        fenetre.fill(background_colour)
        pygame.draw.rect(fenetre, (255,204,204), pygame.Rect(50, 50, width-100, height-100))
        fenetre.blit(iconfond, (500,210))
        if sexe == 1:
            fenetre.blit(persofemme, (20,250))
        elif sexe == 2:
            fenetre.blit(persohomme, (20,250))

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
                    # Variables qui contiennent le nom des options en fonction de la spécialité et création des textes avec le nom du choix de spécialité et du choix de métier
                    nomduchoix = smallfont.render(choix , True , color)
                    nomdumetier = smallfont.render(choixmetier , True , color)
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
                            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                                fin = True
                                edu = False     #On arrête la boucle
                                pygame.display.quit()
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
                                    if 710 <= mouse[0] <= 710+30 and 362 <= mouse[1] <= 362+30:
                                        choixmetier = option02
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                    if 710 <= mouse[0] <= 710+30 and 462 <= mouse[1] <= 462+30:
                                        choixmetier = option03
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                    if 710 <= mouse[0] <= 710+30 and 562 <= mouse[1] <= 562+30:
                                        choixmetier = option04
                                        nomdumetier = smallfont.render(choixmetier , True , color)
                                    if 710 <= mouse[0] <= 710+30 and 662 <= mouse[1] <= 662+30:
                                        choixmetier = option05
                                        nomdumetier = smallfont.render(choixmetier , True , color)

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
                            fenetreedu.blit(nommaternelle , (100,200))
                        # Primaire
                        if 6 < variableage < 12:
                            fenetreedu.blit(nomprimaire , (100,200))
                        # Collège
                        if 11 < variableage < 16:
                            fenetreedu.blit(nomcollege , (100,200))
                        # Lycée
                        if 15 < variableage < 19:
                            fenetreedu.blit(nomlycee , (100,200))

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
                            fenetreedu.blit(specialite , (100,200))

                        # Code pour le fonctionnement du choix des métiers
                        if variableage == 24:
                            # Détection du choix de spécialité fait avant et créations des 5 options
                            # In range 8 car il y a 9 spés
                            for i in range (8):
                                # Code mathématique pour déterminer et calculer les options en fonctions de la spécialité
                                if choix == listeuniversite[i]:
                                    a=i*5
                                    option1 = smallfont.render(dicometiers[a] , True , color)
                                    option01 = dicometiers[a]
                                    option2 = smallfont.render(dicometiers[a+1] , True , color)
                                    option02 = dicometiers[a+1]
                                    option3 = smallfont.render(dicometiers[a+2] , True , color)
                                    option03 = dicometiers[a+2]
                                    option4 = smallfont.render(dicometiers[a+3] , True , color)
                                    option04 = dicometiers[a+3]
                                    option5 = smallfont.render(dicometiers[a+4] , True , color)
                                    option05 = dicometiers[a+4]

                            # Affichage des textes des choix de métiers
                            fenetreedu.blit(option1 , (800,250))
                            fenetreedu.blit(option2 , (800,350))
                            fenetreedu.blit(option3 , (800,450))
                            fenetreedu.blit(option4 , (800,550))
                            fenetreedu.blit(option5 , (800,650))

                            # Affichage du choix selectionné
                            fenetreedu.blit(nomdumetier , (200,250))

                            # Mise en place des rectangles des boutons qui changent de couleurs si la souris est au-dessus
                            if 710 <= mouse[0] <= 710+30 and 262 <= mouse[1] <= 262+30:
                                pygame.draw.rect(fenetreedu,color_bred,[710,262,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[710,262,30,30])
                            if 710 <= mouse[0] <= 710+30 and 362 <= mouse[1] <= 362+30:
                                pygame.draw.rect(fenetreedu,color_bred,[710,362,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[710,362,30,30])
                            if 710 <= mouse[0] <= 710+30 and 462 <= mouse[1] <= 462+30:
                                pygame.draw.rect(fenetreedu,color_bred,[710,462,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[710,462,30,30])
                            if 710 <= mouse[0] <= 710+30 and 562 <= mouse[1] <= 562+30:
                                pygame.draw.rect(fenetreedu,color_bred,[710,562,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[710,562,30,30])
                            if 710 <= mouse[0] <= 710+30 and 662 <= mouse[1] <= 662+30:
                                pygame.draw.rect(fenetreedu,color_bred,[710,662,30,30])
                            else:
                                pygame.draw.rect(fenetreedu,color_dred,[710,662,30,30])

                        # Affichage du métier choisis après les études
                        if variableage > 24:
                            fenetreedu.blit(nomdumetier , (100,200))


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
                        pygame.draw.rect(fenetreprop,color_red,[80,190,326,550])
                        pygame.draw.rect(fenetreprop,color_red,[427,190,326,550])
                        pygame.draw.rect(fenetreprop,color_red,[774,190,326,550])

                        # Affichage des noms des catégories
                        fenetreprop.blit(domicile , (160,200))
                        fenetreprop.blit(transport , (500,200))
                        fenetreprop.blit(animal , (860,200))

                        # Contenu des catégories
                        if choixdomicile==[]:
                            fenetreprop.blit(aucun , (95,400))
                            fenetreprop.blit(domicile1 , (170,450))
                        if 100 <= mouse[0] <= 100+286 and 600 <= mouse[1] <= 600+100:
                            pygame.draw.rect(fenetreprop,color_dred,[100,600,286,100])
                        else:
                            pygame.draw.rect(fenetreprop,color_bred,[100,600,286,100])
                        fenetreprop.blit(acheter , (150,600))
                        fenetreprop.blit(domicile1 , (170,650))

                        if choixtransport==[]:
                            fenetreprop.blit(aucun , (445,400))
                            fenetreprop.blit(transport1 , (510,450))
                        if 447 <= mouse[0] <= 447+286 and 600 <= mouse[1] <= 600+100:
                            pygame.draw.rect(fenetreprop,color_dred,[447,600,286,100])
                        else:
                            pygame.draw.rect(fenetreprop,color_bred,[447,600,286,100])
                        fenetreprop.blit(acheter , (500,600))
                        fenetreprop.blit(transport1 , (510,650))

                        if choixanimal==[]:
                            fenetreprop.blit(aucun , (790,400))
                            fenetreprop.blit(animal1 , (880,450))
                        if 794 <= mouse[0] <= 794+286 and 600 <= mouse[1] <= 600+100:
                            pygame.draw.rect(fenetreprop,color_dred,[794,600,286,100])
                        else:
                            pygame.draw.rect(fenetreprop,color_bred,[794,600,286,100])
                        fenetreprop.blit(acheter , (840,600))
                        fenetreprop.blit(animal1 , (880,650))

                        # Boucle pour les évènements et pour fermer la page
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                                    fin = True
                                    prop = False     #On arrête la boucle
                                    pygame.display.quit()
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    prop=False

                                if 100 <= mouse[0] <= 100+286 and 600 <= mouse[1] <= 600+100: #domicile
                                    dom=True
                                    while dom:
                                        pygame.display.update()
                                        fenetredom = pygame.display.set_mode((width,height))
                                        fenetredom.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetredom,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetredom,color_dark,[50,50,125,50])
                                        fenetredom.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                                                    fin = True
                                                    prop = False     #On arrête la boucle
                                                    pygame.display.quit()

                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    dom=False


                                if 447 <= mouse[0] <= 447+286 and 600 <= mouse[1] <= 600+100: #transport
                                    tra=True
                                    while tra:
                                        pygame.display.update()
                                        fenetretra = pygame.display.set_mode((width,height))
                                        fenetretra.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetretra,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetretra,color_dark,[50,50,125,50])
                                        fenetretra.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                                                    fin = True
                                                    prop = False     #On arrête la boucle
                                                    pygame.display.quit()

                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    tra=False

                                if 794 <= mouse[0] <= 794+286 and 600 <= mouse[1] <= 600+100: #animal
                                    ani=True
                                    while ani:
                                        pygame.display.update()
                                        fenetreani = pygame.display.set_mode((width,height))
                                        fenetreani.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetreani,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetreani,color_dark,[50,50,125,50])
                                        fenetreani.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                                                    fin = True
                                                    prop = False     #On arrête la boucle
                                                    pygame.display.quit()

                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    ani=False




## Page bien-être (mini-jeu)

                # Ouverture de la page bien-être
                if 900 <= mouse[0] <= 900+200 and 500 <= mouse[1] <= 500+50:
                    # Variable bien pour ouvrir et fermer la page bien-être
                    bien=True
                    # Boucle pour la page bien-être
                    while bien:
                        # création de la fenêtre
                        pygame.display.update()
                        fenetrebien = pygame.display.set_mode((width,height))

                        # importer, changer la taille et charger l'arriere plan
                        back = pygame.image.load('image1.jpg')
                        background =pygame.transform.scale(back,(width,height))

                        # charger le game
                        game = Game()

                        # variable pour faire tourner le jeu
                        running= True

                        #boucle tant que cette condition est vrai
                        while running:
                            mouse = pygame.mouse.get_pos()
                            # appliquer l'arriere plan
                            fenetrebien.blit(background, (0, 0))
                            #appliquer l'image du vaisseau
                            fenetrebien.blit(game.vaisseau.image,game.vaisseau.rect)

                            # Bouton retour à la page principale
                            if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                pygame.draw.rect(fenetrebien,color_light,[50,50,125,50])
                            else:
                                pygame.draw.rect(fenetrebien,color_dark,[50,50,125,50])

                            fenetrebien.blit(retour , (60,50))

                            #recuperer les projectiles du vaisseau
                            for projectile in game.vaisseau.x_projectiles:
                                projectile.move()

                            # appliquer l'image du projectiles
                            game.vaisseau.x_projectiles.draw(fenetrebien)

                            #ajouter un son pour le projectile
                            son = pygame.mixer.Sound('laser.mp3')
                            # verifier si le joueur veut aller a gauche ou a droite
                            if game.pressed.get(pygame.K_RIGHT) and game.vaisseau.rect.x + game.vaisseau.rect.width < fenetrebien.get_width():
                                game.vaisseau.move_right()
                            elif game.pressed.get(pygame.K_LEFT) and game.vaisseau.rect.x > 0:
                                game.vaisseau.move_left()
                            # mettre à jour l'ecran
                            pygame.display.flip()

                            # Boucle pour les évènements et pour fermer la page
                            for event in pygame.event.get():
                                #evenement= fermeture de la fenetre
                                if event.type == pygame.QUIT:
                                    running= False
                                    pygame.quit()

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                        pygame.display.update()
                                        bien=False
                                        running= False

                                #detecter si on lache une touche du clavier
                                elif event.type == pygame.KEYDOWN:
                                    game.pressed[event.key]= True
                                    #detecter si la touche espace est enclenchée pour lancer un projectile
                                    if event.key == pygame.K_SPACE:
                                        game.vaisseau.lancer_projectile()
                                        son.play()

                                elif event.type == pygame.KEYUP:
                                    game.pressed[event.key]= False

## Bouton age

                # Variation de l'age si le bouton + une année est cliqué
                if 525 <= mouse[0] <= 525+200 and 510 <= mouse[1] <= 510+100:
                    # Le joueur peut avancer d'un an s'il à moins de 100 ans
                    if variableage < 100:
                        # Ajout du salaire annuel après avoir un métier
                        if variableage > 24:
                            variableargent = variableargent + (salaire*12)
                            argent = bigfont.render(str(variableargent)+"  "+'€', True , color)
                            fenetre.blit(argent , (865,125))
                        # Si tout est bon, la variable variableage s'incrémente de 1 et le texte de l'age est rafraichît
                        if variableage != 19 and variableage != 24:
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                        # Il ne peut pas avancer d'un an s'il n'a pas choisi de spécialité à 19 ans
                        elif variableage == 19 and choix == "":
                            # hide main window
                            root = tkinter.Tk()
                            root.withdraw()
                            tkinter.messagebox.showinfo("Information","Il faut choisir une spécialité!")
                        # Si une spécialité est choisie il peut avancer
                        elif variableage == 19 and choix != "":
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                        # Il ne peut pas avancer d'un an s'il n'a pas choisi de métier à 24 ans
                        elif variableage == 24 and choixmetier == "":
                            # hide main window
                            root = tkinter.Tk()
                            root.withdraw()
                            tkinter.messagebox.showinfo("Information","Il faut choisir un métier!")
                        # Si un métier est choisi il peut avancer et recevra son premier salaire
                        elif variableage == 24 and choixmetier != "":
                            variableage = variableage+1
                            age = smallfont.render('Age:'+"  "+str(variableage) , True , color)
                            variableargent = variableargent + (salaire*12)
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
                        # Affichage du texte de fin
                        fenetretermine.blit(termine , (60,350))
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
        pygame.draw.rect(fenetre,color_dark,[70,100,365,100])
        if sexe == 1:
            fenetre.blit(nomfemme , (75,105))
        elif sexe == 2:
            fenetre.blit(nomhomme , (75,105))
        fenetre.blit(age , (75,145))

        # Affichage du montant de l'argent
        pygame.draw.rect(fenetre,color_dark,[850,100,250,120])
        fenetre.blit(argent , (865,125))

        # Affichage des textes de la page principale sur les boutons par superposition
        fenetre.blit(plus , (615,510))
        fenetre.blit(annee , (546,550))
        fenetre.blit(education , (923,300))
        fenetre.blit(propriete , (925,400))
        fenetre.blit(bienetre , (922,500))
        fenetre.blit(retourmenu , (945,600))

        # Update le display du jeu
        pygame.display.update()
        pygame.display.flip()


## Fonction du début du jeu (premier menu)

# Code pour le menu du départ en utilisant la bibliothèque pygame_menu
def depart():
    menu = pygame_menu.Menu(800, 1200, 'ONLIFE',theme=mytheme)
    logo= menu.add_image('icon.png')
    menu.add_button('Jouer', sexe)
    menu.add_button('Option', option_the_game)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(fenetre)
    return depart()


## Faire tourner le jeu

# Commencer et faire tourner le jeu
depart()


# Code pour pouvoir fermer la page et pour la rafraichir
continuer = True
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = False
    #Rafraichissement
    pygame.display.flip()
