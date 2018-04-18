#clase para el metodo 
# de monte carlos 
# by: Armando Rojas 

class MonteC():
	"""docstring for MonteC"""
	def __init__(self):
		# diana de 25%
		self.probabilidad = 0.25
		self.tabla = {}

	def addTabla(self):
		
		#evento
		self.tabla['x'] = [ 1 , 2 ,3 ,4]
		#probabilidad
		self.tabla['p'] = [ self.probabilidad ,  self.probabilidad * 2  , self.probabilidad * 3 , self.probabilidad * 4]

	def hola(self):
		print("Hola")
		