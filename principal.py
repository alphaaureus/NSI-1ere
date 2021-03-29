import pygame
from game import Game

pygame.init()

pygame.mixer.pre_init(buffer = 256)
# generer la fenetre du jeu
pygame.display.set_caption("mini jeux")
ecran=pygame.display.set_mode((1200,720))
# importer et charger l'arriere plan
background = pygame.image.load('image1.jpg')
play_button =pygame.image.load('play-button.jpg')
play_button = pygame.transform.scale(play_button,(300,50))
play_button_rect=play_button.get_rect()
play_button_rect.x=450
play_button_rect.y=250

# charger le game
game = Game()

running= True

#boucle tant que cette condition est vrai
while running:
    # appliquer l'arriere plan
    ecran.blit(background,(0,0))
    # verifier si notre jeu a commencé ou non
    if game.enroute:
        #déclencher les instruction de la partie
        game.update(ecran)
    else:
        ecran.blit(play_button,play_button_rect)
    # ajouter un son pour le projectile
    son = pygame.mixer.Sound('laser.mp3')
    # mettre à jour l'ecran
    pygame.display.flip()
    # si on ferme la fenetre
    for event in pygame.event.get():
        #evenement= fermeture de la fenetre
        if event.type == pygame.QUIT:
            running= False
            pygame.quit()

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
        elif event.type== pygame.MOUSEBUTTONDOWN:
            #on verifie si la souris a cliquer sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeux en marche
                game.enroute=True


