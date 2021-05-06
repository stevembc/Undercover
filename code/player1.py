import pygame
from data import *

class nehoc(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.points = 1
        self.min_points = 0
        self.image = pygame.image.load('img/sprite_player/nehoc/PNG/attack_1_000.png')
        #self.image = pygame.transform.scale(self.image, (100,100)) modifie la taille de l'image
        self.rect = self.image.get_rect(center = (WIDTH/3,HEIGHT/1.5))
