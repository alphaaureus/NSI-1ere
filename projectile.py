import pygame
#class qui va géner le projectile du vaisseau
class Projectile(pygame.sprite.Sprite):
    def __init__(self, vaisseau):
        super().__init__()
        self.velocity= 5
        self.image= pygame.image.load('laser.png')
        self.image= pygame.transform.scale(self.image,(5,50))
        self.rect= self.image.get_rect()
        self.rect.x= vaisseau.rect.x+57
        self.rect.y= vaisseau.rect.y-40
        self.vaisseau = vaisseau







    #definir le mouvement du projectile
    def move(self):
        self.rect.y -= self.velocity
        #verifier si le projectile depasse la taille de l'ecran
        if self.rect.y < 0:
            self.vaisseau.x_projectiles.remove(self)
        if self.vaisseau.game.check_collision(self,self.vaisseau.game.meteorevent.all_meteor):
            self.vaisseau.x_projectiles.remove(self)
        if self.vaisseau.game.check_collision(self,self.vaisseau.game.all_boss):
            self.vaisseau.game.boss.domage(self.vaisseau.attack)
            self.vaisseau.x_projectiles.remove(self)

class Tirer:
    #interval de tire
    def __init__(self):
        self.pourcentage = 0
        self.pourcentage_v = 500

    def add_pourcentage(self):
        self.pourcentage +=self.pourcentage_v/100
    def full_barre_p(self):
        if self.pourcentage>=100:
            return self.pourcentage>=100
    def ajouter_bar_p(self,ecran):
        #ajouer du pourcentage a la barre
        self.add_pourcentage()
        pygame.draw.rect(ecran,(0,0,0),[0,
                                        ecran.get_height()+20,
                                        ecran.get_width(),
                                        10])
        pygame.draw.rect(ecran, (255, 255, 255), [0,
                                            ecran.get_height()+20,
                                            (ecran.get_width()/100)*self.pourcentage,
                                            10])


