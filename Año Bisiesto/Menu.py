from  Validate  import *

class Menu():
	"""docstring for Menu"""
	def get(self):
		
		print "####################"
		print "##     MENU       ##"
		print "####################"
		print "\n"
		print "( a ) Intervalo Year Bisiestos y No Bisiestos"
		print "( b ) Intervalo Year Bisiestos "
		print "( c ) Intervalo No Bisiestos"
		print "( d ) Consulta de un Year Bisiesto o no Biciesto"
		print "( x ) Salir"

		return raw_input("Escribe la letra de la Opcion correspondiente > ")

	def getIntervalo(self):

		valida = Validate()

		intervalo = { 'inicio' : 0 , 'fin' : 0}; 

		while intervalo['inicio'] == 0:

			intervalo['inicio'] = valida.numInt( raw_input("Escribe el Inicio del Intervalo > ") )

			if( valida.rango(intervalo['inicio'] , 0 , 9999) == False ):
				print "EL year debe estar entre 1 y 9999"
				intervalo['inicio'] = 0



		while intervalo['fin'] == 0:
			intervalo['fin'] = valida.numInt( raw_input("Escribe el Fin del Intervalo > ") )

			if  (valida.intervalo( intervalo['inicio'] , intervalo['fin'] ) == False ):
				print "El Fin del Intervalo debe ser mayor que el de Inicio -> " , intervalo['inicio'] 
				intervalo['fin'] = 0

			if(  valida.rango(intervalo['fin'] , 0 , 9999) == False ):
				print "EL year debe estar entre 1 y 9999"
				intervalo['fin'] = 0


		return intervalo

	def getNumero(self):

		valida = Validate()

		numero = 0 

		while numero == 0:

			numero = valida.numInt( raw_input("Escribe un numero > ") )

			if( valida.rango(numero , 0 , 9999) == False ):
				print "EL year debe estar entre 1 y 9999"
				numero = 0

		return numero

