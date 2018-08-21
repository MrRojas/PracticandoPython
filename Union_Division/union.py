# El formato separado
formato = ("nº 0000-0" , "-0000  (ID: ",   " #)" )
# El numero a unir con el formato
numero = "167"

# por cada tupla hace una union con el numero 
factura = numero.join(formato)

print(factura)