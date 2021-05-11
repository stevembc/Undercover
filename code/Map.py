import pygame
import random

listeMap = [pygame.image.load('img/map/bar_ang.jpeg'),
            pygame.image.load('img/map/bar_fr.jpeg'),
            pygame.image.load('img/map/bar_rus.jpeg'),
            pygame.image.load('img/map/hotel.jpeg'),
            pygame.image.load('img/map/inc.jpeg'),
            pygame.image.load('img/map/toit.jpeg')]
random.random()
zone = random.choice(listeMap)







"""class Map_alea(pygame.sprite.Sprite):

    def __init__(self, lieu):
        super().__init__()
        if lieu == "bar_ang":
            self.bar_ang = pygame.image.load('img/map/bar_ang.jpeg')
            self.bar_ang_rect = self.bar_ang.get_rect(center = (WIDTH/2,HEIGHT/2))

        elif lieu == "bar_fr":
            self.bar_fr = pygame.image.load('img/map/bar_fr.jpeg')
            self.bar_fr_rect = self.bar_fr.get_rect(center = (WIDTH/2,HEIGHT/2))

        elif lieu == "bar_rus":
            self.bar_rus = pygame.image.load('img/map/bar_rus.jpeg')
            self.bar_rus_rect = self.bar_fr.get_rect(center = (WIDTH/2,HEIGHT/2))"""

#self.map = ["bar_ang", "bar_fr", "bar_rus", "hotel", "inc", "toit"]