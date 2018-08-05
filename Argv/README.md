# Argumentos por linea de Comandos 

## Para usarlo debemos importar la libreria necesaria 

```
 import sys
```

se importa **sys** porque posee un metodo para obtener los elementos por linea de comandos 

## Ejemplo 

```
# -*- coding: iso-8859-15
	import sys
	if len(sys.argv) >= 2:
	        print "La cadena introducida tiene",len(sys.argv[1]),"caracteres";
	else:
	        print "Este programa necesita un parámetro";
```

## De aqui tomo mi investigacion: 

http://www.holamundo.es/lenguaje/python/articulos/acceder-argumentos-pasados-parametro-python.html