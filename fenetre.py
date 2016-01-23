import pygame
from pygame.locals import *
from point import *
from personnage import *
from structure import *

class game:

	def __init__(self):
		#Ouverture de la fenêtre Pygame
		self.fenetre = pygame.display.set_mode((800, 600))

		#Chargement de l'image de fond
		self.fond = pygame.image.load("images/fond.png")

		#Collage de l'image fond au coord 0,0
		self.fenetre.blit(self.fond, (0,0))
		
		#affichage des collages
		pygame.display.flip()


	def afficherFond(self):
		self.fenetre.blit(self.fond, (0,0))

	def afficherPerso(self, perso):
		perso.afficher(self)

	def afficherStruct(self, struct):
		struct.afficher(self)

	def afficherPattern(self, pattern):
		pattern.afficher(self)

	def refresh(self, perso, struct, pattern):
		afficherFond(self)
		perso.afficher(perso, self)
		#afficherStruct(stuct, self)
		#afficherPattern(pattern, self)
		pygame.display.flip()


