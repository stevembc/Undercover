import pygame
from data import *

class nehoc(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/map/bar_ang.jpeg')
        self.rect = self.image.get_rect()