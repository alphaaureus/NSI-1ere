import pygame

#class qui va géner le projectile du vaisseau
class Projectile(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super().__init__()
        self.velocity= 5
        self.image= pygame.image.load('projectile.jpg')
        self.image= pygame.transform.scale(self.image,(50,50))
        self.rect= self.image.get_rect()
        self.rect.x= vaisseau.rect.x+37
        self.rect.y= vaisseau.rect.y-40
        self.vaisseau = vaisseau

    #definir le mouvement du projectile
    def move(self):
        self.rect.y -= self.velocity
        #verifier si le projectile depasse la taille de l'ecran
        if self.rect.y > 720:
            #supprimer le projectile
            self.remove()
    #fonction qui supprime le projectile
    def remove(self):
        self.vaisseau.x_projectiles.remove(self)