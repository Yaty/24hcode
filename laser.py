from personnage import *
#from game import *
from case import *

class laser:

	def __init__(self):
		self.liste=[]
		
		
	
	def __str__(self):
		s=""
		for i in range (len(self.liste)):
			s+=" "+str(self.liste[i])
			
		return s
		
	def setDepart(self,perso):
		self.liste=[]
		self.liste.append(self.getCase(perso))
	
	def getCase(self,perso):
		c = case()
		c.caseLaser(perso)
		return c
		
	
	def nextCase(self):
		taille = len(self.liste)
		c = case()
		if(taille==1 and self.liste[0].x==0):
			
			c.setCoord(self.liste[0].x+1, self.liste[0].y)
			
		elif(taille==1 and self.liste[0].x==20):
			
			c.setCoord(self.liste[0].x-1, self.liste[0].y)
		
		elif(taille==1 and self.liste[0].y==0):
			c.setCoord(self.liste[0].x, self.liste[0].y+1)
			
		elif(taille==1 and self.liste[0].y==15):
			c.setCoord(self.liste[0].x, self.liste[0].y-1)
			
		else:
			print("coucou ! \n")
			tempo_x = self.liste[taille-1].x - self.liste[taille-2].x
			tempo_y = self.liste[taille-1].y - self.liste[taille-2].y
			
			c.setCoord(self.liste[taille-1].x+tempo_x,self.liste[taille-1].y+tempo_y)
			
		
			
		return c
		
	def toucheBord(self):
		taille = len(self.liste)
		
		if(self.liste[taille-1].x == 0 or self.liste[taille-1].x == 20  or self.liste[taille-1].y == 0  or self.liste[taille-1].y == 15):
			return False
		
		return True 
		
	
	
	def tirer(self,perso):
		self.setDepart(perso)
		self.liste.append(self.nextCase())
		
		continuer=True
		
		while(continuer):
			self.liste.append(self.nextCase())
			continuer = self.toucheBord()
		
		
		
perso = personnage(400,600)
laz = laser()
print("Laser avant tir : "+str(laz))


laz.tirer(perso)


print("Laser après tir : "+str(laz))



	
