import pygame
from data import *

class Tableau(pygame.sprite.Sprite):

    #Dfinitions du player 
    def __init__(self):
        super().__init__()

        #Caractéristique graphique
        self.image = pygame.image.load('img/interface/tableau.png') #Taille du player 
        self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))    

    #attribuer un mot au hasard aux joueurs.
    #une def pour les synonymes, choisir un mot parmis 6 mots, pendant 3 tours.
    #une def pour soumettre un domaines qui apparait au bout des 4 tours.
    #Re la def pour les synonymes