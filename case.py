from point import *
from bloc import *
import math


class case:
	
	def __init__(self):
		self.typeCase=-1
		self.x=0
		self.y=0
		
	def setCase(self, bloc):
		self.typeCase=bloc.type
		self.x=int(bloc.point.getAbs() /40)
		self.y=int(bloc.point.getOrd() /40)
		
	def caseLaser(self, perso):
		self.type=-1
		self.x=int(perso.get_x()/40)
		self.y=int(perso.get_y()/40)
		
	def setCoord(self,x,y):
		self.x=x
		self.y=y
		
		
	def __str__(self):
		s=""
		s+="Les coordonnees de la case sont :("
		s+=str(self.x) +","+ str(self.y) +") "
		s+="Le type de la case est : "+str(self.typeCase) +"\n"
		return s
	
	
"""b = bloc(200,200,1)

c = case()

c.setCase(b)


print(c)"""
		
		
	
	
		
	
		
	
		
