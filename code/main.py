from data import *
from player import *
from game import *
import pygame

pygame.init()
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Undercover")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))


#Accueil
fnd = pygame.image.load('img/accueil/fnd.jpeg') #Background
accueil = pygame.image.load('img/accueil/start.png') #Icon du jeux
accueil = pygame.transform.scale(accueil, (150, 150)) #La taille
accueil_rect = accueil.get_rect(center = (WIDTH/2,HEIGHT/6)) #L'emplacement
#Dossier perssonnage
nehoc = pygame.image.load('img/accueil/dossier.png') #Dossier 1
nehoc_rect = nehoc.get_rect(center = (WIDTH/7,HEIGHT/2))
voltaire = pygame.image.load('img/accueil/dossier.png') #Dossier 2
voltaire_rect = voltaire.get_rect(center = (WIDTH/2.75,HEIGHT/2))
casey = pygame.image.load('img/accueil/dossier.png') #Dossier 3
casey_rect = casey.get_rect(center = (WIDTH/1.60,HEIGHT/2))
drozdov = pygame.image.load('img/accueil/dossier.png') #Dossier 4
drozdov_rect = drozdov.get_rect(center = (WIDTH/1.15,HEIGHT/2))

#Map   
background = pygame.image.load('img/map/bar_ang.jpeg')

game = Game()
#Background aléatoire

while True:

    display_surface.blit(fnd, (0,0))

    if game.is_playing:
        display_surface.blit(background, (0,0)) #ICI j'ajoute la map généré aléatoirement
    else:
        display_surface.blit(accueil, accueil_rect)
        display_surface.blit(nehoc, nehoc_rect)
        display_surface.blit(voltaire, voltaire_rect)
        display_surface.blit(casey, casey_rect)
        display_surface.blit(drozdov, drozdov_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if accueil_rect.collidepoint(event.pos):
                game.start()
                

    pygame.display.flip()
    pygame.display.update()
    frame_per_sec.tick(60)