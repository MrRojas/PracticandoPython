from  Validate  import *
from  Menu import *

#inicializar variable 
opc = "z"
menu = Menu()
valida = Validate()

while opc != 'x':
	
	opc = menu.get().lower()
	print "\n\n\n\n"
	if opc == "a" or opc == "b" or opc == "c":

		intervalo = menu.getIntervalo()

		for i in xrange(intervalo['inicio']  , intervalo['fin'] +1 ):

			if(valida.bisiesto(i) and opc == "a"):
 				print "El year  " , i , " Si es bisiesto "
			elif(opc == "a"):
				print "El year  " , i , " No es bisiesto "


			if(valida.bisiesto(i) and opc == "b" ):
 				print "El year  " , i 

 			if(valida.bisiesto(i) == False and opc == "c" ):
 				print "El year  " , i 


 	elif opc == "d":

 		numero = menu.getNumero()

		if(valida.bisiesto(numero)):
			print "El year  " , numero , " Si es bisiesto "
		else:
			print "El year  " , numero , " No es bisiesto "
	print "\n\n\n\n"