import math
class Punto():
	
	x = 0
	y = 0
	
	def __init__(self,x1,y1,x2,y2,x3,y3):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		
	
	def distancia(self):
		print("Mis coordenadas son :",self.x1,self.y1,self.x2,self.y2,self.x3,self.y3)
		d1 = math.sqrt((self.x2-self.x1)**2+((self.y2-self.y1)**2))
		d2 = math.sqrt((self.x1-self.x3)**2+((self.y1-self.y3)**2))
		d3 = math.sqrt((self.x3-self.x2)**2+((self.y3-self.y2)**2))
		p=d1+d2+d3
		print("Y mi perimetro es  es de",p," metros")

def principal():
	p = Punto ( x1 = 1, y1 = 1 , x2 = 3, y2 = 5, x3 = 4, y3 = 2 )
	p.distancia()
	


if __name__=="__main__":
	principal()
	