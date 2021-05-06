import pygame
from data import *
from player1 import nehoc
#from player2 import j2

pygame.init()
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Undercover")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))


background = pygame.image.load('img/map/hotel.jpeg')

all_sprite = pygame.sprite.Group()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display_surface.blit(background, (0,0))

    for entity in all_sprite:
        display_surface.blit(entity.surf, entity.rect)
        

    pygame.display.flip()
    pygame.display.update()
    frame_per_sec.tick(60)