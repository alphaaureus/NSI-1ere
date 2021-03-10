import pygame
from game import Game

pygame.init()

pygame.mixer.pre_init(buffer = 256)
# generer la fenetre du jeu
pygame.display.set_caption("mini jeux")
ecran=pygame.display.set_mode((1080,720))
# importer et charger l'arriere plan
background = pygame.image.load('image1.jpg')
# charger le game
game = Game()

running= True

#boucle tant que cette condition est vrai
while running:
    # appliquer l'arriere plan
    ecran.blit(background, (0, 0))
    #appliquer l'image du vaisseau
    ecran.blit(game.vaisseau.image,game.vaisseau.rect)
    #recuperer les projectiles du vaisseau
    for projectile in game.vaisseau.x_projectiles:
        projectile.move()
    # appliquer l'image du projectiles
    game.vaisseau.x_projectiles.draw(ecran)

    #appliquer l'image du boss
    ecran.blit(game.boss.image, game.boss.rect)




    #ajouter un son pour le projectile
    son = pygame.mixer.Sound('laser.mp3')
    # verifier si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.vaisseau.rect.x + game.vaisseau.rect.width < ecran.get_width():
        game.vaisseau.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.vaisseau.rect.x > 0:
        game.vaisseau.move_left()
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
            if event.key == pygame.K_SPACE:
                game.vaisseau.lancer_projectile()
                son.play()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key]= False





