import pygame
from pygame.locals import *

class game:

	def __init__(self):
		#Ouverture de la fenêtre Pygame
		self.fenetre = pygame.display.set_mode((800, 600))
		self.fond = pygame.image.load("images/fond.png")
		self.fenetre.blit(self.fond, (0,0))
		pygame.display.flip()

	def afficherFond(self):
		self.fenetre.blit(self.fond, (0,0))

	def afficherPerso(self, perso):
		


	def refresh(self, perso):

