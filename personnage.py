#!/usr/bin/python3.4.3+
#-*- coding: utf-8 -*-

class personnage:

	def __init__(self):
		self.point = point()
		self.point.x = x
		self.point.y = y

	def set_x(self, incr_x):
		self.point.x += incr_x

	def set_y(self, incr_y):
		self.point.y += incr_y

	def get_x(self):
		return self.point.x

	def get_y(self):
		return self.point.y

	#def tirer(self):
		# On va tirer