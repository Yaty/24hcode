from personnage import *

class laser:

	def __init__(self,perso):
		self.liste=[]
		self.liste.append(perso.point)
		
	
	def __str__(self):
		s=""
		for i in range (len(self.liste)):
			s+=" "+str(self.liste[i])
			
		return s
		
	


		
		
		
