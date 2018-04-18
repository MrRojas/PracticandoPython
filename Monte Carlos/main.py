from MonteC import *

x = MonteC()
# numero de lanzamientos 
num = 16

print ("Probabilidad de lanzamiento de Diana con")
print ("metodo Monte Carlos, by: Armando Rojas")

# aleatorio diana
aleatorioD = 0
#aleatorio flecha
aleatorioF = 0
#aleatorio Diana y flecha 
aleatorioDF = 0

for i in range(0,num):
			
	aleatorioD = random.random()
	aleatorioF = random.random()


	print("##################")
	print()
	print()
	print("lanzamiento " , (i+1))
	print()
	print(" Numero aleatorio de la Diana ->", aleatorioD)
	print(" Diana ->", (x.buscar(aleatorioD) + 1)  )
	print()
	print(" Numero aleatorio de lanzamiento de Flecha ->", aleatorioD)
	print(" lanzamiento de Flecha ->", (x.buscar(aleatorioD) + 1)  )
	print()
	print(" Promedio entre Lanzamiento de Flecha y Diana ->", x.promedio(aleatorioD,aleatorioF) )
	print("  Resultado ->", (x.buscar(x.promedio(aleatorioD,aleatorioF)) + 1)  )




