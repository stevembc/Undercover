import pygame
from data import *

class Nehoc(pygame.sprite.Sprite):

    #Dfinitions du player 
    def __init__(self):
        super().__init__()

        #Caractéristique graphique
        self.image = pygame.image.load('img/sprite_player/nehoc/PNG/attack_1_001.png') #Taille du player
        self.image = pygame.transform.scale(self.image, (SIZE, LENGTH)) 
        self.rect = self.image.get_rect(center = (WIDTH/5,HEIGHT/1.5))


