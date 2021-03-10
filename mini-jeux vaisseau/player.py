import pygame
from projectile import Projectile
pygame.init()


#creer la class vaisseau
class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health= 100
        self.max_health= 100
        self.attack =10
        self.velocity=5
        self.image= pygame.image.load("vaisseau.png")
        self.rect =self.image.get_rect()
        self.rect.x=400
        self.rect.y=600
        self.x_projectiles= pygame.sprite.Group()
    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def lancer_projectile(self):
        self.x_projectiles.add(Projectile(self))

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1000
        self.max_health = 1000
        self.attack = 5
        self.velocity = 0
        self.image = pygame.image.load("vaisseau_boss1.png")
        self.rect = self.image.get_rect()
        self.rect.x= -210
        self.rect.y= -20
