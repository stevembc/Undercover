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


""" une def pour le cumule de points
    Au bout de 1 points tu peux soumettre un mot
    Au bout de 2 points tu peux montrer la première lettre de l'adversaire ou montrer le domaine du mot adverse
    Au bout de 3 points tu peux montrer la dernière lettre de l'adversaire
    Au bout de 4 points tu peux montrer le nombre de lettre
"""
    #Après chaque nom de domaine le perso obtient 1 point
    #une def pour soumettre un mot et si le mot est les même que celui de l'adversaire: print("win") else print("wrong')

# TROUVER UN MOYEN D'AFFICHER LES VALEURS QUE L'ONT A RENTRÈ

