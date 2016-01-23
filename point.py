import math	
class point:
	def __init__(self):
		self.x=0
		self.y=0
		
	def __init__(self,abs,ord):
		self.x=abs
		self.y=ord
		
		
	def __str__(self):
		s="("+str(self.x)+","+str(self.y)+")\n"
		return s
		
	def distance(self, p2):
		return math.sqrt(math.pow(p2.x-self.x,2)+math.pow(p2.y-self.y,2))
		 
	def getAbs(self):
		return self.x
	
	def getOrd(self):
		return self.y
		
	def setAbs(self,abs):
		self.x=abs
		
	def setOrd(self,ord):
		self.y=ord
		
	
		
	

p1 = point(0,0)
print(p1)

p2=point(2,2)
print(p2)

print("La distance entre p1 est p2 est : "+str(p1.distance(p2))+"\n")
