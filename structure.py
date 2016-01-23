import pygame
from pygame.locals import *
from point import *
from personnage import *
from fenetre import *

class structure:

	def __init__(self, pattern):

		self.blocs = []
		self.taille = 0
		self.pattern = pattern

	def afficher(game, self):

		for i in range(taille):
			self.blocs[i].afficher()
