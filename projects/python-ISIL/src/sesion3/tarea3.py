def principal():
#ejercicio 1:
	mylist=list(range(1,10))
	
	suma=0 
	
	for i in mylist:
		cuadrado = (i**2)
		suma=suma+(i**2)
		print (cuadrado)
		
	print('la suma del cuadrado es:',suma)
	
############################################

#ejercicio 2:

	texto=list('Desperte por la tarde sin saber de mi existencia , el sunset de mis recuerdos , mi recuerdo desaparecio y sin mas memoria volvi a caer en la nostalgia de tus recuerdos y sentimientos que me llevaron a la autodestruccion y sin pensar ya estaba en la otra vida simplemente viendote como caminas por la calle empapada de la lluvia')
	
	c=0
	
	for i in texto:
		if (i == 'a'):
			c = c+1
	print(texto)		
	print('el numero de veces que se repite la letra "A" es de:',c, 'veces	')

	
		
if __name__=="__main__":
	principal()