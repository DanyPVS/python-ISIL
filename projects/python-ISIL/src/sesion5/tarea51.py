import math
class Punto():
	
	x = 0
	y = 0
	
	def __init__(self,x1,y1,x2,y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		
	
	def distancia(self):
		print("Mis coordenadas son :",self.x1,self.y1,self.x2,self.y2)
		d = math.sqrt((self.x2-self.x1)**2+((self.y2-self.y1)**2))
		print("Y mi distancia es de",d," metros")

def principal():
	p = Punto ( x1 = 0, y1 = 0 , x2 = 10, y2 = 0 )
	p.distancia()
	


if __name__=="__main__":
	principal()
	
	