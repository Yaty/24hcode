import pygame
from pygame.locals import *

from personnage import *
from fenetre import *
from structure import *

jeu = game()
p1 = point(110,110)
print(p1)

hanSolo = personnage(100,100)
boucle = 1


i = 0
while(boucle):
	hanSolo.afficher(jeu)
	i = i + 1

