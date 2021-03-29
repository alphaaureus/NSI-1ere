import pygame
from player import Vaisseau
from player import Boss
from meteor import MeteorEvent
from meteor import Meteor
from projectile import Tirer
from projectile import Projectile
#creer une class pour la game
class Game:
    def __init__(self):
        #generer le vaisseau
        self.all_vaisseau=pygame.sprite.Group()
        self.vaisseau = Vaisseau(self)
        self.all_vaisseau.add(self.vaisseau)
        self.pressed = {}
        self.all_boss=pygame.sprite.Group()
        self.boss=Boss(self)
        self.all_boss.add(self.boss)
        self.meteor=Meteor(self)
        self.meteorevent=MeteorEvent(self)
        self.tirer=Tirer()
    enroute=False
    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def update(self, ecran):
        # appliquer l'image du vaisseau
        ecran.blit(self.vaisseau.image, self.vaisseau.rect)
        # recuperer les projectiles du vaisseau
        for projectile in self.vaisseau.x_projectiles:
            projectile.move()
        # appliquer l'image du projectiles
        self.vaisseau.x_projectiles.draw(ecran)
        # actualiser les barres de vie
        self.vaisseau.barre_vie(ecran)
        self.boss.barre_vie_boss(ecran)
        # barre event si on veut l afficher
        self.meteorevent.ajouter_bar(ecran)
        self.tirer.ajouter_bar_p(ecran)
        # appliquer l'image du boss
        ecran.blit(self.boss.image, self.boss.rect)
        for meteor in self.meteorevent.all_meteor:
            meteor.tomber()
        #appliquer les meteor
        self.meteorevent.all_meteor.draw(ecran)
        #appliquer le game over
        self.vaisseau



        # verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.vaisseau.rect.x + self.vaisseau.rect.width < ecran.get_width():
            self.vaisseau.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.vaisseau.rect.x > 0:
            self.vaisseau.move_left()

