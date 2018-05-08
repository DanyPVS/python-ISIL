def principal():
	mylista=[1,12.4,"hola","c++0",True,[1,2]]
	print(len(mylista))
	print(mylista)
	
	lista2=mylista
	print(lista2)
	lista2[2]="chua"
	print(mylista)
	print(lista2)
	
	hola="hola mundo"
	lista_hola=list(hola)
	print(lista_hola)
	print(" ".join(hola))
	
	
	
if __name__=="__main__":
	principal()