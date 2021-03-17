import pygame
from player import Vaisseau
from player import Boss

#creer une class pour la game
class Game:
    def __init__(self):
        #generer le vaisseau
        self.vaisseau = Vaisseau()
        self.pressed = {}
        self.boss=Boss()
