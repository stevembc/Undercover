from data import *
from player import *
from game import *
from tableau import *
from mots import *
import pygame
import random

pygame.init()

frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Undercover")
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))


#Icone du jeux
fnd = pygame.image.load('img/accueil/fnd.jpeg') #Background
fnd = pygame.transform.scale(fnd, (WIDTH, HEIGHT))
accueil = pygame.image.load('img/accueil/start.png') #Icon du jeux
accueil = pygame.transform.scale(accueil, (150, 150)) #La taille
accueil_rect = accueil.get_rect(center = (WIDTH/2,HEIGHT/6)) #L'emplacement
#Dossiers perssonnages
nehoc = pygame.image.load('img/accueil/dossier.png') #Dossier 1
nehoc_rect = nehoc.get_rect(center = (WIDTH/7,HEIGHT/2))
voltaire = pygame.image.load('img/accueil/dossier.png') #Dossier 2
voltaire_rect = voltaire.get_rect(center = (WIDTH/2.75,HEIGHT/2))
casey = pygame.image.load('img/accueil/dossier.png') #Dossier 3
casey_rect = casey.get_rect(center = (WIDTH/1.60,HEIGHT/2))
drozdov = pygame.image.load('img/accueil/dossier.png') #Dossier 4
drozdov_rect = drozdov.get_rect(center = (WIDTH/1.15,HEIGHT/2))

#Map aléaoire  
listeMap = [pygame.image.load('img/map/bar_ang.jpeg'),
            pygame.image.load('img/map/bar_fr.jpeg'),
            pygame.image.load('img/map/bar_rus.jpeg'),
            pygame.image.load('img/map/hotel.jpeg'),
            pygame.image.load('img/map/inc.jpeg'),
            pygame.image.load('img/map/toit.jpeg')]
zone = random.choice(listeMap)
zone = pygame.transform.scale(zone, (WIDTH, HEIGHT))

#FONT


#Appel des classes pour le main
game = Game()
joueur = Nehoc()
table = Tableau()
#synonyme = Synonyme()



all_sprite = pygame.sprite.Group()
all_sprite.add(joueur)
all_sprite.add(table)
#all_sprite.add(synonyme)


#Boucle du jeux
while True:

    #Gameplay
    if game.is_playing:
        display_surface.blit(zone, (0,0))
        #display_surface.blit(synonyme, (WIDTH/1.15,HEIGHT/2))
        
        for entity in all_sprite:
            display_surface.blit(entity.image, entity.rect)  

    #Accueil
    else:
        display_surface.blit(fnd, (0,0))
        display_surface.blit(accueil, accueil_rect)
        display_surface.blit(nehoc, nehoc_rect)
        display_surface.blit(voltaire, voltaire_rect)
        display_surface.blit(casey, casey_rect)
        display_surface.blit(drozdov, drozdov_rect)

    for event in pygame.event.get():
        #Quitter pygame
        if event.type == pygame.QUIT:
            pygame.quit()
        #Evenement au clic
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if nehoc_rect.collidepoint(event.pos):
                game.start()
            if voltaire_rect.collidepoint(event.pos):
                game.start()
            if casey_rect.collidepoint(event.pos):
                game.start()
            if drozdov_rect.collidepoint(event.pos):
                game.start()

    pygame.display.flip()
    pygame.display.update()
    frame_per_sec.tick(60)