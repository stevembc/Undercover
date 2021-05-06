import pygame
from data import *
from player1 import nehoc
#from player2 import j2

pygame.init()
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Undercover")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))


background = pygame.image.load('img/map/hotel.jpeg')
j1 = nehoc()


while True:

    display_surface.blit(background, (0,0))
    display_surface.blit(j1.image, j1.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.flip()
    pygame.display.update()
    frame_per_sec.tick(60)