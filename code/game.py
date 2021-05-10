import pygame
from player import *
from data import *


class Game:

    def __init__(self):
        self.is_playing = False

    def start(self):
        self.is_playing = True

    def game_over(self):
        print("YOU LOOSE")

""" def update(self, background):
        display_surface.blit(background, background_rect)
        display_surface.blit(self.player.image, self.player.rect)
        display_surface.blit(j1.image, j1.rect)"""