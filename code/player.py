import pygame
from data import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.point = 1
        self.image = pygame.image.load('img/sprite_player/nehoc/PNG/attack_1_000.png')
        #self.image = pygame.transform.scale(self.image, (100,100)) modifie la taille de l'image
        self.rect = self.image.get_rect(center = (WIDTH/4,HEIGHT/1.5))

