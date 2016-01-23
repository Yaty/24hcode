import pygame
from pygame.locals import *
from point import *
from personnage import *
from fenetre import *

class structure:

	def __init__(self, typeStruct, taille):
		self.blocs = []
		self.type = typeStruct
		self.taille = taille
		
	def addBloc(self, bloc):
		self.blocs.append(bloc)

	def afficher(self, game):
		for i in range(self.taille):
			self.blocs[i].afficher(game)
