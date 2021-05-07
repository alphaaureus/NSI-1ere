import pygame
from projectile import Projectile
pygame.init()

#creer la class vaisseau
class Vaisseau(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health= 100
        self.max_health= 100
        self.attack =10
        self.velocity=5
        self.image= pygame.image.load("vaisseau.png")
        self.rect =self.image.get_rect()
        self.rect.x=400
        self.rect.y=600
        self.x_projectiles= pygame.sprite.Group()
    #fonction qui gère les degats reçu du vaisseau
    def damage(self,somme):
        #infliger des degats en fonction de la vie restante
        if self.health - somme> somme or self.health - somme <= somme :
            self.health -= somme
        if self.health <= 0:
            self.game.enroute=False
            self.health = self.health + 100
            self.game.boss.health=1050

    #fonction de la barre de vie
    def barre_vie(self,ecran):
        #on dessine 2 rectangle qui fais office de barre de vie
        pygame.draw.rect(ecran,(60,63,60),[self.rect.x+10,self.rect.y -10,self.max_health,5])
        pygame.draw.rect(ecran, (111, 210, 46), [self.rect.x + 10, self.rect.y -10, self.health, 5])

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def lancer_projectile(self):
        self.x_projectiles.add(Projectile(self))
#creer la class Boss
class Boss(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 1050
        self.max_health = 1050
        self.attack = 5
        self.velocity = 0
        self.image = pygame.image.load("vaisseau_boss.png")
        self.rect = self.image.get_rect()
        self.rect.x= 85
        self.rect.y= 50
        self.game=game
    def barre_vie_boss(self,ecran):
        pygame.draw.rect(ecran,(60,63,60),[self.rect.x+10,self.rect.y +130,self.max_health,5])
        pygame.draw.rect(ecran, (111, 210, 46), [self.rect.x + 10, self.rect.y +130, self.health, 5])
    #fonction qui gère les degats reçu du Boss
    def domage(self,somme):
        #infliger des degats de la vie restante
        if self.health - somme >= somme or self.health - somme <= somme :
            self.health -= somme
        if self.health <= 0:
            self.game.gain=True
            self.game.enroute=False
            self.health=self.health+1050
            self.game.vaisseau.health=100