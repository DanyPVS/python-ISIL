def principal():
	mydict={}
	mydict={
		"red":"das50",
		"black":"das3d",
		"blu":"d3350",	
	}
	
	mydict["negro"]="fffff"
	print(mydict)
	print (list(mydict.keys()))
	
	import ipdb
	ipdb.set_trace()
	
	for key,value in mydict.items():
		print(key,"-"*3+">",value)

	
if __name__=="__main__":
	principal()