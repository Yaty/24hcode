#!/usr/bin/python3.4.3+
#-*- coding: utf-8 -*-

from point import *

class personnage:

	def __init__(self):
		self.point = point(0,0)
		

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

	def afficher(fenetre):
		self.fenetre = pygame.image.load("./images/perso.png")
		self.fenetre


	#def tirer(self):
		# On va tirer
