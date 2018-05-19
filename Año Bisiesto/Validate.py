# Clase para realizar validaciones
class Validate():
	
	# Validar que un caracter sea la letra S o N 
	def rspSiNo(self):
		#inicializar 
		rsp = "x"
		# mientras la rsp no sea s o n pide opcion 
		while rsp !=("s") and rsp !=("n"):
			# obtener datos de entrada transdormado en miniscula 
			rsp = raw_input( "Elije S para Si o N para no > " ).lower()
		return rsp 

	# valida un numero entero 
	def numInt(self , cadena):
		try:
			# intenta transformar 
			num = int(cadena)
		except ValueError:
			# si no es un numero devuelve 0
			num = 0
		return num
	#valida el inicio del intervalo que sea menor que el fin del intervalo
	def intervalo(self, i , f):
		
		if i < f:
			return True
		else:
			return False

	#valida el rango de un determinado numero 
	def rango(self,num,  min , max):
		
		if num > max or num < min:
			return False
		else: 
			return True
	# valida si un year es bisiesto
	def bisiesto(self , i):

		if(i % 4 == 0 and i % 100 != 0 or i % 400 == 0):
			return True
		else:
			return False


