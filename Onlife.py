#Importation des bibliothèques
import pygame
import pygame_menu
import random
from random import randint
from pygame.locals import *
from game import Game
from player import Vaisseau
from projectile import Projectile



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

imagesfemmes=[femme1,femme2,femme3,femme4]
imageshommes=[homme1,homme2,homme3,homme4,homme5]

# Images de décoration
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
salaire = 0


#Listes pour la page enseignement
listematernelle=["Ecole maternelle Béré","Ecole maternelle Le Coudray","Ecole maternelle Henri Bergson","Ecole maternelle Jules Ferry","Ecole maternelle Claude Monet","Ecole maternelle Prince Bois","Ecole maternelle Le Bourgeau","Ecole maternelle du Massif","Ecole maternelle Molière","Ecole maternelle du Centre"]
listeprimaire=["Ecole primaire Guillaume Apollinaire","Ecole primaire Michel Servet","Ecole primaire Albert Barraud","Ecoles primaire les Néréides","Ecole primaire Jean Jaurès","Ecole primaire Jacques Prévert","Ecole primaire Charles Perrault","Ecole primaire La Clé des Champs","Ecole primaire Les Nondales","Ecole primaire L'Arbre Enchanté"]
listecollege=["Collège Chaptal","Collège Plaisance","Collège Jean Giono","Collège les Fontainettes","Collège Victor Hugo","Collège des Trois Vallées","Collège la Sablière","Collège Antoine de Saint-Exupéry","Collège Claude Nicolas le Doux","Collège Les Franchises"]
listelycee=["Lycée Jean Rostand","Lycée Henri Vincenot","Lycée Camille Claudel","Lycée Pasteur","Lycée Gustave Eiffel","Lycée Voltaire","Lycée Parc des Loges","Lycée Martin Luther King","Lycée Honoré Romane","Lycée Jean Monnet"]
listeuniversite=["Commerce","Ingénieur","Lettres","Arts","Politique","Sc.Sociales","Droit","Architecture","Médecine"]
dicometiers=[["Caissier",1750],["Commercial",4108],["Acheteur",3500],["Ag.Immobilier",3500],["Ag.Marketing",5083],["Aéronautique",5100],["Chimie",5500],["Environnement",2000],["Génie Civil",4750],["Mécanique",2300],["Ecrivain",2767],["Libraire",2000],["Traducteur",2500],["Editeur",5000],["Enseignant",3500],["Illustrateur",3986],["Photographe",1430],["Sculpteur",1800],["Peintre",4400],["Galeriste",2240],["Ministre",14900],["Politologue",1430],["Diplomate",3700],["Maire",8454],["Parlementaire",8757],["Démographe",3600],["Ethnologue",2500],["Historien",1500],["Sociologue",2160],["Assistant soc.",1700],["Avocat",2600],["Juge",4447],["Notaire",8700],["Huissier",8000],["Greffier",2580],["Architecte",3300],["Urbaniste",2800],["Décorateur",4000],["Installateur",2000],["Coloriste",1700],["Médecin",10684],["Pharmacien",3850],["Psychologie",3200],["Chirurgien",11500],["Infirmier",1800]]
listedomicile=[["Studio - 1",98],["Studio - 2",127],["Studio - 3",75],["Studio - 4",82],["Studio - 5",250],["Appart - 1",249],["Appart - 2",450],["Appart - 3",330],["Appart - 4",279],["Appart - 5",427],["Maison - 1",985],["Maison - 2",824],["Maison - 3",675],["Maison - 4",310],["Maison - 5",639],["Villa - 1",1690],["Villa - 2",2780],["Villa - 3",3150],["Villa - 4",1330],["Villa - 5",1490]]
listetransport=[["Vélo - 1",1.75],["Vélo - 2",4.6],["Moto - 1",5.9],["Moto - 2",10.3],["Berline - 1",15.5],["Berline - 2",22.3],["Break - 1",16.6],["Break - 2",19.2],["Monospace - 1",23.6],["Monospace - 2",28.1],["Citadines - 1",16.2],["Citadines - 2",22.9],["4x4 - 1",29],["4x4 - 2",31.8],["Limousine - 1",47],["Limousine - 2",72],["Bateau - 1",159],["Bateau - 2",385],["Jet Privé - 1",2950],["Jet Privé - 2",5000]]
listeanimal=[["Chien - 1",1000],["Chien - 2",1500],["Chat - 1",1000],["Chat - 2",1250],["Poisson - 1",150],["Poisson - 2",250],["Furet - 1",2500],["Furet - 2",3250],["Cheval - 1",6000],["Cheval - 2",9750],["Lapin - 1",3500],["Lapin - 2",4450],["Hamster - 1",1700],["Hamster - 2",2250],["Oiseau - 1",5250],["Oiseau - 2",8750],["Poule - 1",200],["Poule - 2",500],["Cochon - 1",3750],["Cochon - 2",6500]]


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
    # Couleur blanche du texte
    color = (255,255,255)
    color2= (0,0,0)

    # Couleurs pour les différents rectangles de fond
    color_light = (170,170,170)
    color_dark = (100,100,100)

    # Police du texte avec deux tailles différentes
    smallfont = pygame.font.SysFont('comicsansms',35)
    smallfont2 = pygame.font.SysFont('comicsansms',25)
    bigfont = pygame.font.SysFont('comicsansms',50)
    bigfont2 = pygame.font.SysFont('comicsansms',40)

    # Textes
    retour = smallfont.render('retour' , True , color)
    ligne1 = bigfont.render('Bienvenu à Onlife!' , True , color2)
    ligne2 = smallfont2.render("Le jeu où vous pouvez vivre la vie dont vous avez tant rêvé!", True , color2)
    ligne3 = smallfont2.render("Vous commencez à l'an 0 avec une somme aléatoire d'argent.", True , color2)
    ligne4 = smallfont2.render("Pour grandir d'une année, appuyez sur la touche '+ une année'.", True , color2)
    ligne5 = smallfont2.render("Au fil de votre vie, vous pouvez choisir vos études, votre métier et jouer au mini-jeu.", True , color2)
    ligne6 = smallfont2.render("Vous avez 100 ans pour vous amuser le plus possible!", True , color2)
    ligne7 = bigfont2.render('Éducation:' , True , color2)
    ligne8 = smallfont2.render("Vous commencez à 3 ans, vous allez à la maternelle, en primaire, au collège puis au lycée.", True , color2)
    ligne9 = smallfont2.render("À 19 ans, vous pouvez choisir votre spécialité et à 23 ans, votre métier.", True , color2)
    ligne10 = bigfont2.render('Propriété:' , True , color2)
    ligne11 = smallfont2.render("Il y a trois catégories de propriété.", True , color2)
    ligne12 = smallfont2.render("Vous pouvez vous rendre en magasin pour acheter un maximum de 7 articles par catégorie.", True , color2)
    ligne13 = bigfont2.render('Bien-être:' , True , color2)
    ligne14 = smallfont2.render("Ici, vous vous lancez dans un jeu complémentaire qui se déroule dans un milieu intergalactique.", True , color2)
    ligne15 = smallfont2.render("Cela vous permet de gagner de l'argent pour vous acheter tout ce dont vous rêvez.", True , color2)

    # Variable pour la boucle option
    optionfin=False

    while not optionfin:
        pygame.display.update()
        # Mise en place de l'affichage de la fenêtre principale
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
        fenetreoption.blit(ligne10, (50,480))
        fenetreoption.blit(ligne11, (50,530))
        fenetreoption.blit(ligne12, (50,560))
        fenetreoption.blit(ligne13, (50,610))
        fenetreoption.blit(ligne14, (50,660))
        fenetreoption.blit(ligne15, (50,690))

        # Bouton retour à la page principale
        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
            pygame.draw.rect(fenetreoption,color_light,[50,50,125,50])
        else:
            pygame.draw.rect(fenetreoption,color_dark,[50,50,125,50])
        fenetreoption.blit(retour , (60,50))

        # Détection d'événements
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                optionfin = True      #On arrête la boucle
                pygame.display.quit() #On ferme le display

            # Vérifie si la souris est cliquée
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Bouton retour
                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                    pygame.display.update()
                    optionfin=True
                    depart()


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
    variableargent = randint(100, 100000)

    # Variables pour les erreurs
    erreur = 0
    erreur2 = 0
    erreurani = 0

    #Variable pour les différentes pages et boucles du jeu
    fin = False
    edu=False
    jeu=False
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
    game_colour1 = (105,105,105)
    game_colour2 = (128,128,128)

    # Police du texte avec deux tailles différentes
    minifont = pygame.font.SysFont('comicsansms',30)
    smallfont = pygame.font.SysFont('comicsansms',35)
    mediumfont = pygame.font.SysFont('comicsansms',40)
    bigfont = pygame.font.SysFont('comicsansms',50)
    bigfont3 = pygame.font.SysFont('comicsansms',60)

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
    termine = bigfont.render("Vous avez atteint 100 ans, le jeu est terminé!" , True , color)
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
    minijeu = bigfont3.render("Mini-Jeu" , True , color)

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
    magasin = bigfont.render('Magasin' , True , color)
    maximumdom = minifont.render("Vous n'avez pas assez d'argent ou vous avez atteint le maximum de domiciles!" , True , color_dark)
    maximumtra = minifont.render("Vous n'avez pas assez d'argent ou vous avez atteint le maximum de transports!" , True , color_dark)
    maximumani = minifont.render("Vous n'avez pas assez d'argent ou vous avez atteint le maximum d'animaux!" , True , color_dark)


    # Texte de la page bien-être
    bienetre = smallfont.render('Bien-être' , True , color)
    bienbig = bigfont.render('Bien-être' , True , color)
    Basique = smallfont.render('Basique:' , True , color)
    Médium = smallfont.render('Médium:' , True , color)
    Luxe = smallfont.render('Luxe:' , True , color)
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
                                                fenetrejeu.blit(background, (0, 0))
                                                #appliquer l'image du vaisseau
                                                fenetrejeu.blit(game.vaisseau.image,game.vaisseau.rect)

                                                # Bouton retour à la page principale
                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.draw.rect(fenetrejeu,color_light,[50,50,125,50])
                                                else:
                                                    pygame.draw.rect(fenetrejeu,color_dark,[50,50,125,50])

                                                fenetrejeu.blit(retour , (60,50))

                                                #recuperer les projectiles du vaisseau
                                                for projectile in game.vaisseau.x_projectiles:
                                                    projectile.move()

                                                # appliquer l'image du projectiles
                                                game.vaisseau.x_projectiles.draw(fenetrejeu)

                                                #appliquer l'image du boss
                                                fenetrejeu.blit(game.boss.image, game.boss.rect)


                                                #ajouter un son pour le projectile
                                                son = pygame.mixer.Sound('laser.mp3')
                                                # verifier si le joueur veut aller a gauche ou a droite
                                                if game.pressed.get(pygame.K_RIGHT) and game.vaisseau.rect.x + game.vaisseau.rect.width < fenetrejeu.get_width():
                                                    game.vaisseau.move_right()
                                                elif game.pressed.get(pygame.K_LEFT) and game.vaisseau.rect.x > 0:
                                                    game.vaisseau.move_left()
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
                                                        if event.key == pygame.K_SPACE:
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
                            fenetreedu.blit(nomlycee , (150,185))
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
                        # Domicile
                        if choixdomicile==[]:
                            fenetreprop.blit(aucun , (95,400))
                            fenetreprop.blit(domicile1 , (170,450))
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
                        fenetreprop.blit(domicile1 , (170,675))

                        # Transport
                        if choixtransport==[]:
                            fenetreprop.blit(aucun , (445,400))
                            fenetreprop.blit(transport1 , (510,450))
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
                        fenetreprop.blit(transport1 , (510,675))

                        # Animal
                        if choixanimal==[]:
                            fenetreprop.blit(aucun , (790,400))
                            fenetreprop.blit(animal1 , (880,450))
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
                        fenetreprop.blit(animal1 , (880,675))

                        # Boucle pour les évènements et pour fermer la page
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    prop=False

### domicile

                                if 100 <= mouse[0] <= 100+286 and 625 <= mouse[1] <= 625+100:
                                    dom=True
                                    # Variable pour les erreurs
                                    erreurdom = 0
                                    while dom:
                                        pygame.display.update()
                                        fenetredom = pygame.display.set_mode((width,height))
                                        fenetredom.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()
                                        #Titre
                                        pygame.draw.rect(fenetredom,color_dark,[230,25,900,100])
                                        fenetredom.blit(magasin , (580,40))
                                        # Affichage des options de domiciles
                                        x=0
                                        largeur=75

                                        for i in range (2):
                                            hauteur=200
                                            for i in range (10):
                                                ledomicile=listedomicile[x][0]
                                                ledomicileprix=listedomicile[x][1]
                                                ledomiciletexte1 = smallfont.render(listedomicile[x][0] , True , color)
                                                ledomiciletexte2 = smallfont.render(str(listedomicile[x][1])+" K" , True , color)
                                                # Rectangle de couleur différente pour savoir si l'objet à déjà été acheté
                                                if listedomicile[x][0] in choixdomicile:
                                                    pygame.draw.rect(fenetredom,color_dred,[largeur-10,hauteur+5,460,43])
                                                else:
                                                    pygame.draw.rect(fenetredom,color_bred,[largeur-10,hauteur+5,460,43])
                                                fenetredom.blit(ledomiciletexte1 , (largeur,hauteur))
                                                fenetredom.blit(ledomiciletexte2 , (largeur+330,hauteur))
                                                hauteur=hauteur+50
                                                x=x+1
                                            largeur=largeur+600

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetredom,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetredom,color_dark,[50,50,125,50])
                                        fenetredom.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                # Bouton retour
                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    dom=False

                                                # Détection choix du domicile
                                                #1
                                                if 65 <= mouse[0] <= 460+65 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listedomicile[0][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[0][1]*1000)
                                                        choixdomicile.append(listedomicile[0][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #2
                                                if 65 <= mouse[0] <= 460+65 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listedomicile[1][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[1][1]*1000)
                                                        choixdomicile.append(listedomicile[1][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #3
                                                if 65 <= mouse[0] <= 460+65 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listedomicile[2][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[2][1]*1000)
                                                        choixdomicile.append(listedomicile[2][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #4
                                                if 65 <= mouse[0] <= 460+65 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listedomicile[3][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[3][1]*1000)
                                                        choixdomicile.append(listedomicile[3][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #5
                                                if 65 <= mouse[0] <= 460+65 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listedomicile[4][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[4][1]*1000)
                                                        choixdomicile.append(listedomicile[4][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #6
                                                if 65 <= mouse[0] <= 460+65 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listedomicile[5][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[5][1]*1000)
                                                        choixdomicile.append(listedomicile[5][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #7
                                                if 65 <= mouse[0] <= 460+65 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listedomicile[6][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[6][1]*1000)
                                                        choixdomicile.append(listedomicile[6][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #8
                                                if 65 <= mouse[0] <= 460+65 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listedomicile[7][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[7][1]*1000)
                                                        choixdomicile.append(listedomicile[7][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #9
                                                if 65 <= mouse[0] <= 460+65 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listedomicile[8][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[8][1]*1000)
                                                        choixdomicile.append(listedomicile[8][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #10
                                                if 65 <= mouse[0] <= 460+65 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listedomicile[9][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[9][1]*1000)
                                                        choixdomicile.append(listedomicile[9][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #11
                                                if 665 <= mouse[0] <= 460+665 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listedomicile[10][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[10][1]*1000)
                                                        choixdomicile.append(listedomicile[10][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #12
                                                if 665 <= mouse[0] <= 460+665 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listedomicile[11][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[11][1]*1000)
                                                        choixdomicile.append(listedomicile[11][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #13
                                                if 665 <= mouse[0] <= 460+665 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listedomicile[12][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[12][1]*1000)
                                                        choixdomicile.append(listedomicile[12][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #14
                                                if 665 <= mouse[0] <= 460+665 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listedomicile[13][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[13][1]*1000)
                                                        choixdomicile.append(listedomicile[13][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #15
                                                if 665 <= mouse[0] <= 460+665 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listedomicile[14][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[14][1]*1000)
                                                        choixdomicile.append(listedomicile[14][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #16
                                                if 665 <= mouse[0] <= 460+665 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listedomicile[15][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[15][1]*1000)
                                                        choixdomicile.append(listedomicile[15][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #17
                                                if 665 <= mouse[0] <= 460+665 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listedomicile[16][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[16][1]*1000)
                                                        choixdomicile.append(listedomicile[16][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #18
                                                if 665 <= mouse[0] <= 460+665 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listedomicile[17][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[17][1]*1000)
                                                        choixdomicile.append(listedomicile[17][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #19
                                                if 665 <= mouse[0] <= 460+665 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listedomicile[18][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[18][1]*1000)
                                                        choixdomicile.append(listedomicile[18][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1
                                                #20
                                                if 665 <= mouse[0] <= 460+665 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listedomicile[19][1]*1000) and len(choixdomicile)<7:
                                                        variableargent = variableargent - (listedomicile[19][1]*1000)
                                                        choixdomicile.append(listedomicile[19][0])
                                                        erreurdom=0
                                                    else:
                                                        erreurdom=erreurdom+1

                                        # Blit des erreurs
                                        if erreurdom > 0:
                                            fenetredom.blit(maximumdom , (60,720))


### transport

                                if 447 <= mouse[0] <= 447+286 and 625 <= mouse[1] <= 625+100:
                                    tra=True
                                    # Variable pour les erreurs
                                    erreurtra = 0
                                    while tra:
                                        pygame.display.update()
                                        fenetretra = pygame.display.set_mode((width,height))
                                        fenetretra.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()
                                        #Titre
                                        pygame.draw.rect(fenetretra,color_dark,[230,25,900,100])
                                        fenetretra.blit(magasin , (580,40))
                                        # Affichage des options de domiciles
                                        x=0
                                        largeur=75
                                        for i in range (2):
                                            hauteur=200
                                            for i in range (10):
                                                letransport=listetransport[x][0]
                                                letransportprix=listetransport[x][1]
                                                letransporttexte1 = smallfont.render(listetransport[x][0] , True , color)
                                                letransporttexte2 = smallfont.render(str(listetransport[x][1])+" K", True , color)
                                                # Rectangle de couleur différente pour savoir si l'objet à déjà été acheté
                                                if listetransport[x][0] in choixtransport:
                                                    pygame.draw.rect(fenetretra,color_dred,[largeur-10,hauteur+5,460,43])
                                                else:
                                                    pygame.draw.rect(fenetretra,color_bred,[largeur-10,hauteur+5,460,43])
                                                fenetretra.blit(letransporttexte1 , (largeur,hauteur))
                                                fenetretra.blit(letransporttexte2 , (largeur+330,hauteur))
                                                hauteur=hauteur+50
                                                x=x+1
                                            largeur=largeur+600

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetretra,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetretra,color_dark,[50,50,125,50])
                                        fenetretra.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:

                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    tra=False

                                                # Détection choix du transport
                                                #1
                                                if 65 <= mouse[0] <= 460+65 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listetransport[0][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[0][1]*1000)
                                                        choixtransport.append(listetransport[0][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #2
                                                if 65 <= mouse[0] <= 460+65 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listetransport[1][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[1][1]*1000)
                                                        choixtransport.append(listetransport[1][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #3
                                                if 65 <= mouse[0] <= 460+65 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listetransport[2][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[2][1]*1000)
                                                        choixtransport.append(listetransport[2][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #4
                                                if 65 <= mouse[0] <= 460+65 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listetransport[3][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[3][1]*1000)
                                                        choixtransport.append(listetransport[3][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #5
                                                if 65 <= mouse[0] <= 460+65 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listetransport[4][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[4][1]*1000)
                                                        choixtransport.append(listetransport[4][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #6
                                                if 65 <= mouse[0] <= 460+65 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listetransport[5][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[5][1]*1000)
                                                        choixtransport.append(listetransport[5][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #7
                                                if 65 <= mouse[0] <= 460+65 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listetransport[6][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[6][1]*1000)
                                                        choixtransport.append(listetransport[6][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #8
                                                if 65 <= mouse[0] <= 460+65 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listetransport[7][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[7][1]*1000)
                                                        choixtransport.append(listetransport[7][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #9
                                                if 65 <= mouse[0] <= 460+65 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listetransport[8][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[8][1]*1000)
                                                        choixtransport.append(listetransport[8][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #10
                                                if 65 <= mouse[0] <= 460+65 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listetransport[9][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[9][1]*1000)
                                                        choixtransport.append(listetransport[9][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #11
                                                if 665 <= mouse[0] <= 460+665 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listetransport[10][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[10][1]*1000)
                                                        choixtransport.append(listetransport[10][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #12
                                                if 665 <= mouse[0] <= 460+665 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listetransport[11][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[11][1]*1000)
                                                        choixtransport.append(listetransport[11][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #13
                                                if 665 <= mouse[0] <= 460+665 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listetransport[12][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[12][1]*1000)
                                                        choixtransport.append(listetransport[12][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #14
                                                if 665 <= mouse[0] <= 460+665 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listetransport[13][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[13][1]*1000)
                                                        choixtransport.append(listetransport[13][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #15
                                                if 665 <= mouse[0] <= 460+665 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listetransport[14][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[14][1]*1000)
                                                        choixtransport.append(listetransport[14][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #16
                                                if 665 <= mouse[0] <= 460+665 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listetransport[15][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[15][1]*1000)
                                                        choixtransport.append(listetransport[15][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #17
                                                if 665 <= mouse[0] <= 460+665 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listetransport[16][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[16][1]*1000)
                                                        choixtransport.append(listetransport[16][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #18
                                                if 665 <= mouse[0] <= 460+665 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listetransport[17][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[17][1]*1000)
                                                        choixtransport.append(listetransport[17][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #19
                                                if 665 <= mouse[0] <= 460+665 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listetransport[18][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[18][1]*1000)
                                                        choixtransport.append(listetransport[18][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1
                                                #20
                                                if 665 <= mouse[0] <= 460+665 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listetransport[19][1]*1000) and len(choixtransport)<7:
                                                        variableargent = variableargent - (listetransport[19][1]*1000)
                                                        choixtransport.append(listetransport[19][0])
                                                        erreurtra=0
                                                    else:
                                                        erreurtra=erreurtra+1

                                        # Blit des erreurs
                                        if erreurtra > 0:
                                            fenetretra.blit(maximumtra , (60,720))

### animal

                                if 794 <= mouse[0] <= 794+286 and 625 <= mouse[1] <= 625+100:
                                    ani=True
                                    # Variable pour les erreurs
                                    erreurani = 0
                                    while ani:
                                        pygame.display.update()
                                        fenetreani = pygame.display.set_mode((width,height))
                                        fenetreani.fill(background_colour)
                                        mouse = pygame.mouse.get_pos()
                                        #Titre
                                        pygame.draw.rect(fenetreani,color_dark,[230,25,900,100])
                                        fenetreani.blit(magasin , (580,40))
                                        # Affichage des options de domiciles
                                        x=0
                                        largeur=75
                                        for i in range (2):
                                            hauteur=200
                                            for i in range (10):
                                                lanimal=listeanimal[x][0]
                                                lanimalprix=listeanimal[x][1]
                                                lanimaltexte1 = smallfont.render(listeanimal[x][0] , True , color)
                                                lanimaltexte2 = smallfont.render(str(listeanimal[x][1]) , True , color)
                                                # Rectangle de couleur différente pour savoir si l'objet à déjà été acheté
                                                if listeanimal[x][0] in choixanimal:
                                                    pygame.draw.rect(fenetreani,color_dred,[largeur-10,hauteur+5,460,43])
                                                else:
                                                    pygame.draw.rect(fenetreani,color_bred,[largeur-10,hauteur+5,460,43])
                                                fenetreani.blit(lanimaltexte1 , (largeur,hauteur))
                                                fenetreani.blit(lanimaltexte2 , (largeur+350,hauteur))
                                                hauteur=hauteur+50
                                                x=x+1
                                            largeur=largeur+600

                                        # Bouton retour à la page propriété
                                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                            pygame.draw.rect(fenetreani,color_light,[50,50,125,50])
                                        else:
                                            pygame.draw.rect(fenetreani,color_dark,[50,50,125,50])
                                        fenetreani.blit(retour , (60,50))

                                        # Boucle pour les évènements
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                                    pygame.display.update()
                                                    ani=False

                                                # Détection choix de l'animal
                                                #1
                                                if 65 <= mouse[0] <= 460+65 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listeanimal[0][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[0][1])
                                                        choixanimal.append(listeanimal[0][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #2
                                                if 65 <= mouse[0] <= 460+65 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listeanimal[1][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[1][1])
                                                        choixanimal.append(listeanimal[1][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #3
                                                if 65 <= mouse[0] <= 460+65 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listeanimal[2][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[2][1])
                                                        choixanimal.append(listeanimal[2][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #4
                                                if 65 <= mouse[0] <= 460+65 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listeanimal[3][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[3][1])
                                                        choixanimal.append(listeanimal[3][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #5
                                                if 65 <= mouse[0] <= 460+65 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listeanimal[4][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[4][1])
                                                        choixanimal.append(listeanimal[4][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #6
                                                if 65 <= mouse[0] <= 460+65 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listeanimal[5][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[5][1])
                                                        choixanimal.append(listeanimal[5][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #7
                                                if 65 <= mouse[0] <= 460+65 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listeanimal[6][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[6][1])
                                                        choixanimal.append(listeanimal[6][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #8
                                                if 65 <= mouse[0] <= 460+65 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listeanimal[7][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[7][1])
                                                        choixanimal.append(listeanimal[7][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #9
                                                if 65 <= mouse[0] <= 460+65 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listeanimal[8][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[8][1])
                                                        choixanimal.append(listeanimal[8][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #10
                                                if 65 <= mouse[0] <= 460+65 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listeanimal[9][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[9][1])
                                                        choixanimal.append(listeanimal[9][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #11
                                                if 665 <= mouse[0] <= 460+665 and 205 <= mouse[1] <= 43+205:
                                                    if variableargent > (listeanimal[10][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[10][1])
                                                        choixanimal.append(listeanimal[10][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #12
                                                if 665 <= mouse[0] <= 460+665 and 255 <= mouse[1] <= 43+255:
                                                    if variableargent > (listeanimal[11][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[11][1])
                                                        choixanimal.append(listeanimal[11][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #13
                                                if 665 <= mouse[0] <= 460+665 and 305 <= mouse[1] <= 43+305:
                                                    if variableargent > (listeanimal[12][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[12][1])
                                                        choixanimal.append(listeanimal[12][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #14
                                                if 665 <= mouse[0] <= 460+665 and 355 <= mouse[1] <= 43+355:
                                                    if variableargent > (listeanimal[13][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[13][1])
                                                        choixanimal.append(listeanimal[13][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #15
                                                if 665 <= mouse[0] <= 460+665 and 405 <= mouse[1] <= 43+405:
                                                    if variableargent > (listeanimal[14][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[14][1])
                                                        choixanimal.append(listeanimal[14][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #16
                                                if 665 <= mouse[0] <= 460+665 and 455 <= mouse[1] <= 43+455:
                                                    if variableargent > (listeanimal[15][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[15][1])
                                                        choixanimal.append(listeanimal[15][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #17
                                                if 665 <= mouse[0] <= 460+665 and 505 <= mouse[1] <= 43+505:
                                                    if variableargent > (listeanimal[16][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[16][1])
                                                        choixanimal.append(listeanimal[16][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #18
                                                if 665 <= mouse[0] <= 460+665 and 555 <= mouse[1] <= 43+555:
                                                    if variableargent > (listeanimal[17][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[17][1])
                                                        choixanimal.append(listeanimal[17][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #19
                                                if 665 <= mouse[0] <= 460+665 and 605 <= mouse[1] <= 43+605:
                                                    if variableargent > (listeanimal[18][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[18][1])
                                                        choixanimal.append(listeanimal[18][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1
                                                #20
                                                if 665 <= mouse[0] <= 460+665 and 655 <= mouse[1] <= 43+655:
                                                    if variableargent > (listeanimal[19][1]) and len(choixanimal)<7:
                                                        variableargent = variableargent - (listeanimal[19][1])
                                                        choixanimal.append(listeanimal[19][0])
                                                        erreurani=0
                                                    else:
                                                        erreurani=erreurani+1

                                        # Blit des erreurs
                                        if erreurani > 0:
                                            fenetreani.blit(maximumani , (60,720))


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

                        # Bouton retour à la page principale
                        if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                            pygame.draw.rect(fenetrebien,color_light,[50,50,125,50])
                        else:
                            pygame.draw.rect(fenetrebien,color_dark,[50,50,125,50])
                        fenetrebien.blit(retour , (60,50))

                        # Titre de la page
                        pygame.draw.rect(fenetrebien,color_dark,[230,25,900,100])
                        fenetrebien.blit(bienbig , (580,40))

                        # Eléments de la page
                        # Rectangles pour le décor
                        pygame.draw.rect(fenetrebien,color_dark,[50,165,1080,600])
                        pygame.draw.rect(fenetrebien,color_red,[80,190,326,550])
                        pygame.draw.rect(fenetrebien,color_red,[427,190,326,550])
                        pygame.draw.rect(fenetrebien,color_red,[774,190,326,550])

                        # Affichage des noms des catégories
                        fenetrebien.blit(Basique , (160,200))
                        fenetrebien.blit(Médium , (500,200))
                        fenetrebien.blit(Luxe , (860,200))

                        # Boucle pour les évènements et pour fermer la page
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 50 <= mouse[0] <= 125+50 and 50 <= mouse[1] <= 50+50:
                                    pygame.display.update()
                                    bien=False


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
        pygame.draw.rect(fenetre,color_dark,[80,100,365,100])
        if sexe == 1:
            fenetre.blit(nomfemme , (85,105))
        elif sexe == 2:
            fenetre.blit(nomhomme , (85,105))
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


## Fonction du début du jeu (premier menu)

# Code pour le menu du départ en utilisant la bibliothèque pygame_menu
def depart():
    menu = pygame_menu.Menu(800, 1200, 'ONLIFE',theme=mytheme)
    logo= menu.add_image('icon.png')
    menu.add_button('Jouer', sexe)
    menu.add_button('Guide', option_the_game)
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