from data import *
from player import Player
from game import *
import pygame

pygame.init()
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Undercover")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

#Accueil
fnd = pygame.image.load('img/accueil/fnd.jpeg')
accueil = pygame.image.load('img/accueil/start.png')
accueil = pygame.transform.scale(accueil, (150, 150))
accueil_rect = accueil.get_rect(center = (WIDTH/2,HEIGHT/3))

#Page 1
background = pygame.image.load('img/map/hotel.jpeg')

game = Game()

while True:

    display_surface.blit(fnd, (0,0))

    if game.is_playing:
        display_surface.blit(background, (0,0))
    else:
        display_surface.blit(accueil, accueil_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if accueil_rect.collidepoint(event.pos):
                game.start()

    pygame.display.flip()
    pygame.display.update()
    frame_per_sec.tick(60)