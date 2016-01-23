#!/usr/bin/python3.4.3+
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from point import *
from fenetre import *
from structure import *


class personnage:

	def __init__(self,x,y):
		self.point = point(x,y)
		self.image = pygame.image.load("images/perso.png")

	def __str__(self):
		s="("+str(self.point.x)+","+str(self.point.y)+")\n"
		return s

	def set_x(self, incr_x):
		self.point.x += incr_x

	def set_y(self, incr_y):
		self.point.y += incr_y

	def get_x(self):
		return self.point.x

	def get_y(self):
		return self.point.y

	def afficher(self, game):
		game.fenetre.blit(self.image, (self.point.x, self.point.y))
		pygame.display.flip()


	#def tirer(self):
		# On va tirer
