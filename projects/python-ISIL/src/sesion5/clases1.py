class Gatos():
	
	nombre = None
	color = "negro"
	tamano = None
	
	def __init__(self,nombre,color,tamano):
		self.nombre = nombre
		self.color = color
		self.tamano = tamano 
		
	
#	def maullar(self):
	#	print("maullar..")
	
	def saludar(self):
		print("hola soy",self.nombre)
	

def principal():
	felix = Gatos (	nombre	="felix",
				 	color	="negro",
				 	tamano	="pequeño")
	felix.maullar()
	felix.saludar()
	
	garfiel


if __name__=="__main__":
	principal()
	
	
