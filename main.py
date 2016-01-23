import pygame
from pygame.locals import *

from personnage import *
from fenetre import *
from structure import *
from bloc import * 

jeu = game()
hanSolo = personnage(0,565)
bloc1 = bloc(100,100, 0)

pattern = structure(0, 3)

matPattern = [(100,100), (140,100), (180,100)]

for i in range(3):
	bloc1 = bloc(matPattern[i][0], matPattern[i][1], 0)
	pattern.addBloc(bloc1)


boucle = 1
i = 0
while(boucle):
	pattern.afficher(jeu)
	hanSolo.afficher(jeu)
	for event in pygame.event.get():
		jeu.refresh(hanSolo, bloc1, pattern)
		hanSolo.actions(event, jeu)

