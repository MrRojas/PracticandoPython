#clase para el metodo 
# de monte carlos 
# by: Armando Rojas 
import random


class MonteC():
	"""docstring for MonteC"""
	def __init__(self):
		# diana de 25%
		self.probabilidad = 0.25
		self.tabla = {}

		#probabilidad  
		self.tabla['p'] = []
		#probabilidad acumulada 
		self.tabla['f'] = []
		#evento
		self.tabla['x'] = []
		#intervalos 
		self.tabla['intervalo'] = []
		#diametro acumulado
		self.tabla['diametroA'] = []
		#diametro 
		self.tabla['diametro'] = []

		self.addTabla()


		self.lanzamientoDiana = {}
		self.lanzamientoFlecha = {}
		self.lanzamientoFlechaDiana = {}



	def addTabla(self):


		for i in range(1,5):
			
			self.tabla['p'].append( self.probabilidad )

			self.tabla['x'].append(i)

			self.tabla['f'].append(self.probabilidad * i)
			
			if i == 1:
				self.tabla['intervalo'].append( [ 0 ,  self.probabilidad ] )
			else:
				# probabilidad anterior 
				anterior = i - 2 
				# probabilidad en el mismo indice
				anterior2 = i - 1
				self.tabla['intervalo'].append( [ self.tabla['intervalo'][anterior][1] , self.tabla['f'][anterior2] ] )
		pass

	def buscar(self , num):

		indice = -1
		encontrado = -1

		for i in self.tabla['intervalo']:

			indice = indice + 1


			if ( num >= i[0]   ) and ( num <= i[1]  ):
				encontrado = indice

			
		return encontrado

	def promedio( self , num1 , num2  ):
		return (num1 + num2) / 2





		
		

