#!/usr/bin/python3.4.3+
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from point import *
from personnage import *
from fenetre import *
from structure import *

class bloc:

	def __init__(self):
		self.point.x = x
		self.point.y = y
		self.l = 40
		self.L = 40

	def __str__(self):
		s="("+str(self.x)+","+str(self.y)+")\n"
		return s

	def set_x(self, coord_x):
		self.point.x = coord_x

	def set_y(self, coord_y):
		self.point.y = coord_y

	def get_x(self):
		return self.point.x

	def get_y(self):
		return self.point.y

	def afficher(self, game):
		

	