import pygame
import random
class Meteor(pygame.sprite.Sprite):
    def __init__(self,meteor_event):
        super().__init__()
        image=['asteroide.png','asteroide1.png','asteroide2.png','asteroide3.png']
        self.image = pygame.image.load(random.choice(image))
        self.rect= self.image.get_rect()
        self.velocity=1
        self.rect.x = random.randint(10,1200)
        self.rect.y =100
        self.meteor_event=meteor_event
        self.attack=10
        vie=[10,20,30]
        self.health=random.choice(vie)
        self.max_health=30

    def tomber(self):
        self.rect.y += self.velocity
        #tombe au sol
        if self.rect.y >=650:
            self.meteor_event.all_meteor.remove(self)
        #verifier si sa touche le vaisseau
        if self.meteor_event.game.check_collision(self,self.meteor_event.game.all_vaisseau):
            #supprimer le meteor et faire des degats
            self.meteor_event.all_meteor.remove(self)
            self.meteor_event.game.vaisseau.damage(self.attack)



class MeteorEvent:
    def __init__(self,game):
        self.pourcentage=0
        self.pourcentage_v=200
        self.game=game
        #groupe de sprite pour les meteor
        self.all_meteor=pygame.sprite.Group()
    #ajouter des pourcentage pour la barre
    def add_pourcentage(self):
        self.pourcentage +=self.pourcentage_v/100
    #fonction qui renvoie le pourcentage
    def full_barre(self):
        return self.pourcentage>=100
    def meteor_s(self):
        #apparaitre un meteor
        self.all_meteor.add(Meteor(self))
    def spawn_meteor(self):
        # si la jauge de labarre est charger a 100
        if self.full_barre():
            self.meteor_s()
            self.pourcentage=0

    def ajouter_bar(self,ecran):
        #ajouer du pourcentage a la barre
        self.add_pourcentage()
        #appeler la fonction spawn meteor
        self.spawn_meteor()
        pygame.draw.rect(ecran,(0,0,0),[0,
                                        ecran.get_height()+10,
                                        ecran.get_width(),
                                        10])
        pygame.draw.rect(ecran, (187, 11, 11), [0,
                                            ecran.get_height()+10,
                                            (ecran.get_width()/100)*self.pourcentage,
                                            10])